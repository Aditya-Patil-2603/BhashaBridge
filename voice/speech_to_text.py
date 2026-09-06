import speech_recognition as sr

LANGUAGE_CODES = {
    "Hindi": "hi-IN",
    "Marathi": "mr-IN",
    "English": "en-IN"
}

def speech_to_text(language="Hindi"):
    lang_code = LANGUAGE_CODES.get(language, "hi-IN")
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(f"🎤 Bolna shuru karo ({language} mein)... (sun raha hoon)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language=lang_code)
        print(f"✅ Tumne kaha: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Samajh nahi aaya, dobara try karo")
        return None
    except sr.RequestError:
        print("❌ Internet connection check karo")
        return None


if __name__ == "__main__":
    speech_to_text(language="Hindi")