from googletrans import Translator

# Initializing the translator
translator = Translator()

# Function to translate text
def translate_text(text, src_language, dest_language):
    """
    Translate text from one language to another.
    
    Parameters:
        text (str): Text to be translated.
        src_language (str): Source language (e.g., 'en' for English, 'es' for Spanish), or leave it empty to detect automatically.
        dest_language (str): Target language (e.g., 'fr' for French, 'de' for German).
        
    Returns:
        tuple: Translated text and detected language (if source language is auto-detected).
    """
    try:
        if src_language:
            translation = translator.translate(text, src=src_language, dest=dest_language)
            return translation.text, src_language
        else:
            detection = translator.detect(text)
            detected_language = detection.lang
            translation = translator.translate(text, src=detected_language, dest=dest_language)
            return translation.text, detected_language
    except Exception as e:
        return f"Error during translation: {e}", None

# User input
print("\n\tSimple Language Translation Tool")
print("\n\tSupported languages: 'en' (English), 'es' (Spanish), 'fr' (French), 'de' (German), etc. \n\tFor a complete list of language codes, visit: https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes")
text = input("\n\tEnter text to translate: ")
src_language = input("\tEnter source language code (leave blank for auto-detection): ").lower()
dest_language = input("\tEnter destination language code: ").lower()

# Translate text
translated_text, detected_language = translate_text(text, src_language, dest_language)

# Print results
if src_language:
    print(f"\n\tSource Language: {src_language} (Provided)")
else:
    print(f"\n\tDetected Language: {detected_language} (Auto-detected)")

print(f"\n\tTranslated Text ({detected_language if not src_language else src_language} -> {dest_language}):\n\t{translated_text}")