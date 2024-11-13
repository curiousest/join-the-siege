from src.openai_clf import openai_classifier
from src.types import BANK_STATEMENT
from unittest import TestCase

# TODO make this an integration test instead of a unit test.
# TODO don't run in CI/CD pipeline.
class TestOpenaiClassifier(TestCase):
    def test_openai_classifier(self):
        with open("./tests/data/bank_statement_1.txt", "r") as f:
            text = f.read()
        
        result = openai_classifier(text)
        self.assertEqual(result, BANK_STATEMENT)