"""translation functions"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """translates english text to french"""
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    french_text = translator.translate(english_text)
    return french_text
def french_to_english(french_text):
    """translates french text to english"""
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    english_text = translator.translate(french_text)
    return english_text

