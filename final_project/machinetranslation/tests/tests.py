"""holla"""
from translator import english_to_french, french_to_english
import unittest

class test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertIsNone(english_to_french(""))

class test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertIsNone(french_to_english(""))
unittest.main()