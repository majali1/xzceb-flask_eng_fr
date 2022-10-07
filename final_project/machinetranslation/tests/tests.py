import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testNullValue(self):
        self.assertIsNotNone(english_to_french('Hello'), 'The input is not null')

    def testTranslation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def testNullValue(self):
        self.assertIsNotNone(french_to_english('Bonjour'), 'The input is not null')

    def testTranslation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()