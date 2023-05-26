from translator import englishToFrench, frenchToEnglish
import unittest

class TestTranslator(unittest.TestCase):
    def test_en2fr(self):
        """
        Test English to French
        """
        # self.assertEqual(englishToFrench(''), '')  # Test empty string returns empty string
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        self.assertEqual(englishToFrench('Bonjour'), 'Bonjour')
    
    def test_fr2en(self):
        """
        Test French to English
        """
        # self.assertEqual(frenchToEnglish(''), '') # Test empty string returns empty string
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        self.assertEqual(frenchToEnglish('Hello'), 'Hello')

unittest.main()
