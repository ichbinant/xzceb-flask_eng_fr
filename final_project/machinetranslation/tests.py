import unittest

from translator import english_to_french, french_to_english

class TestEnglish2French(unittest.TestCase):
    #test from English to French
    def test1(self):
        #Hello returns Bonjour
        self.assertEqual(english_to_french('hello'), 'bonjour')
        #Hello does not return Hello
        self.assertNotEqual(english_to_french('hello'), 'hello')

class TestFrench2English(unittest.TestCase):
    #test from French to English
    def test1(self):
        #Bonjour returns Hello
        self.assertEqual(french_to_english('bonjour'), 'hello')
        #Bonjour does not return Bonjour
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')

unittest.main()





