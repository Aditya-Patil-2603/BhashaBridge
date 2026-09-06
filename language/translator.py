from deep_translator import GoogleTranslator

LANGUAGE_CODES = {
    "Hindi": "hi",
    "Marathi": "mr",
    "English": "en"
}

def translate_text(text, target_language="Hindi"):
    target_code = LANGUAGE_CODES.get(target_language, "hi")

    try:
        translated = GoogleTranslator(source="auto", target=target_code).translate(text)
        return translated
    except Exception as e:
        print(f"❌ Translation error: {e}")
        return text  # agar translation fail ho to original text hi wapas de do


if __name__ == "__main__":
    original = "You need a valid ID proof and address proof to renew your driving licence."

    print("Original (English):", original)
    print("Hindi:", translate_text(original, target_language="Hindi"))
    print("Marathi:", translate_text(original, target_language="Marathi"))