from src.classifier import extract_text_from_file
from unittest import TestCase

class TestPreprocessing(TestCase):
    def test_extract_text_from_file(self):
        with open("./tests/data/bank_statement_1.pdf", "rb") as file:
            text = extract_text_from_file(file)
        
        with open("./tests/data/bank_statement_1.txt", "r") as f:
            expected_text = f.read()
        
        print(text)
        print(expected_text)
        self.maxDiff = None
        self.assertEqual(text, expected_text)
    
    def test_extract_text_from_image(self):
        with open("./tests/data/drivers_license_1.jpg", "rb") as file:
            text = extract_text_from_file(file)

        with open("./tests/data/drivers_licence_1.txt", "r") as f:
            expected_text = f.read()
        
        self.assertEqual(text, expected_text)