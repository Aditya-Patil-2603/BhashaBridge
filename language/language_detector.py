from langdetect import detect, DetectorFactory

# Isse result hamesha consistent aata hai (varna har baar thoda alag aa sakta hai)
DetectorFactory.seed = 0

# langdetect ke language codes ko humare app ke naam se match karna
LANGUAGE_MAP = {
    "hi": "Hindi",
    "mr": "Marathi",
    "en": "English"
}

def detect_language(text):
    try:
        lang_code = detect(text)
        language = LANGUAGE_MAP.get(lang_code, "Unknown")
        return language
    except Exception:
        return "Unknown"


if __name__ == "__main__":
    print(detect_language("मुझे driving licence renew karna hai"))
    print(detect_language("मला पॅन कार्ड काढायचे आहे"))
    print(detect_language("I want to apply for a passport"))