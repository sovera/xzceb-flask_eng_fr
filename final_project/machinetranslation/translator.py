from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    traductor = MyMemoryTranslator(source='es', target='en')
    french_text = traductor.translate(english_text)
    return french_text

def french_to_english(french_text):
    traductor = MyMemoryTranslator(source='es', target='en')
    english_text = traductor.translate(french_text)
    return english_text