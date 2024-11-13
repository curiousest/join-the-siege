from .types import BANK_STATEMENT, INVOICE, DRIVERS_LICENCE, UNKNOWN_FILE

# TODO make these files instead of python files. Fix import paths.
from .data.bank_statement_1 import bank_statement_1
from .data.invoice_1 import invoice_1
from .data.drivers_licence_1 import drivers_licence_1

few_shot_prompt = f"""
You are an AI model that classifies extracted text from documents into four categories: {BANK_STATEMENT}, {INVOICE}, {DRIVERS_LICENCE}, or {UNKNOWN_FILE}. Below are examples of text for each type (except for {UNKNOWN_FILE}). Use these examples to classify new inputs. Your response should be in JSON format, indicating the type of document.

**Examples:**

1. **Example 1: Bank Statement**
   {bank_statement_1}

   **Output:**
   {{
     "type": "bank_statement"
   }}

2. **Example 2: Invoice**
   {invoice_1}

   **Output:**
   {{
     "type": "invoice"
   }}

3. **Example 3: Driver License**
   {drivers_licence_1}

   **Output:**
   {{
     "type": "drivers_licence"
   }}
"""