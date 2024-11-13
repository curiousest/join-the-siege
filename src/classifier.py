import io

import pytesseract
import pypdf
from PIL import Image
from werkzeug.datastructures import FileStorage

from .openai_clf import openai_classifier, CustomException
from .sklearn_clf import sklearn_classifier
from .types import BANK_STATEMENT, INVOICE, DRIVERS_LICENCE, UNKNOWN_FILE
from .utils import CustomException

def classify_file(file: FileStorage) -> str:
    '''
    Classify a file into one of the following types:
    - bank_statement
    - invoice
    - drivers_license
    - unknown
    '''

    try:
        text = extract_text_from_file(file)
    except Exception as e:
        return filename_classifier(file.filename)
    
    # First, attempt to classify using the trained classifier
    try:
        return sklearn_classifier(text)
    except CustomException as e:
        pass

    # If that doesn't work, use OpenAI as a backup
    try:
        return openai_classifier(text)
    except CustomException as e:
        # Finally, if all else fails, use the filename classifier
        return filename_classifier(file.filename)

def filename_classifier(filename: str) -> str:
    filename = filename.lower()

    if "drivers_license" in filename:
        return DRIVERS_LICENCE

    if "bank_statement" in filename:
        return BANK_STATEMENT

    if "invoice" in filename:
        return INVOICE

    return UNKNOWN_FILE

def get_file_type(file: FileStorage) -> str:
    if len(file.name) < 4:
        return "unknown"

    return file.name.split(".")[-1]

def extract_text_from_file(file: FileStorage) -> str:
    file_bytes = file.read()
    file_type = get_file_type(file)
    
    if file_type == "txt":
        return file_bytes.decode("utf-8")
    
    if file_type == "pdf":
        return extract_text_from_pdf(file_bytes)
    
    if file_type in ["jpeg", "png", "jpg"]:
        return extract_text_from_image(file_bytes)
    
    raise ValueError(f"Unsupported file type: {file_type}")

def extract_text_from_pdf(file_bytes: bytes) -> str:
    pdf_reader = pypdf.PdfReader(io.BytesIO(file_bytes))
    return "\n".join([page.extract_text() for page in pdf_reader.pages])

def extract_text_from_image(file_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(file_bytes))
    return pytesseract.image_to_string(image)
