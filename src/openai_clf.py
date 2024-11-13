import os
from openai import OpenAI
from .prompts import few_shot_prompt
from pydantic import BaseModel
from .types import FILE_TYPES, UNKNOWN_FILE


# TODO: move to env
PROJECT_ID = "proj_hUizl3mrZGSfmp4C6DI60dJo"
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
model = 'gpt-4o-mini'

class StatementClassification(BaseModel):
    type: str

# TODO better exception naming
class CustomException(Exception):
    pass

def openai_classifier(text):
    '''
    Classify the text using OpenAI's GPT-4o-mini model. Few-shot prompt is used to guide the model.
    '''
    messages = []
    messages.append({
        "role": "system",
        "content": few_shot_prompt
    })
    
    messages.append({
        "role": "user",
        "content": "Classify the following text:\n" + text
    })

    # TODO more specific exception-handling
    try:
        response = client.beta.chat.completions.parse(model=model, messages=messages, response_format=StatementClassification)
    except Exception as e:
        raise CustomException("OpenAI call failed") from e

    try:
        output = response.choices[0].message.parsed
        #structured_output = json.loads(output)['type'].lower()
    except Exception as e:
        raise CustomException("OpenAI formatting incorrect", response) from e

    if output.type in FILE_TYPES:
        return output.type
    else:
        return UNKNOWN_FILE
