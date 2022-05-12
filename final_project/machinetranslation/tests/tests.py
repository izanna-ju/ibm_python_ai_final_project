import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(" "), " ")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        self.assertEqual(french_to_english(" "), " ")
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main() 