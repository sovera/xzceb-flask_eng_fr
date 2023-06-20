"""Modulo de traduccion de idiomas entre frances e ingles"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Funcion que traduce un texto de ingles a frances"""
    traductor = MyMemoryTranslator(source='en', target='fr')
    french_text = traductor.translate(english_text)
    return french_text

def french_to_english(french_text):
    """Funcion que traduce un texto de frances a ingles"""
    traductor = MyMemoryTranslator(source='fr', target='en')
    english_text = traductor.translate(french_text)
    return english_text
