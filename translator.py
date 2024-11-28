from googletrans import Translator
from language_map import LANGUAGE_MAP

# Initialize translator
translator = Translator()

# Language name to code mapping

# Function to get language code from name
def get_language_code(language_name):
    return LANGUAGE_MAP.get(language_name.lower())

# Function to translate text
def translate_text(text, src_language_name, dest_language_name):
    try:
        # Convert language names to codes
        src_language_code = get_language_code(src_language_name) if src_language_name else None
        dest_language_code = get_language_code(dest_language_name)

        if not dest_language_code:
            return f"Error: Destination language '{dest_language_name}' is not supported."

        # Perform translation
        if src_language_code:
            translation = translator.translate(text, src=src_language_code, dest=dest_language_code)
            detected_language = src_language_name
        else:
            detection = translator.detect(text)
            detected_language = detection.lang
            translation = translator.translate(text, src=detection.lang, dest=dest_language_code)

        return f"\tSource Language: {detected_language.capitalize()}\n\tTranslated Text ({src_language_name} -> {dest_language_name}):\n\t{translation.text}"

    except Exception as e:
        return f"Error during translation: {e}"

# User input
print("\nSimple Language Translation Tool")
print("\n\tSupported languages: English, Spanish, French, German, etc.")

text = input("\n\tEnter text to translate: ")
src_language = input("\tEnter source language (leave blank for auto-detection): ").lower()
dest_language = input("\tEnter destination language: ").lower()

# Translate text
result = translate_text(text, src_language, dest_language)
print(f"\n{result}")