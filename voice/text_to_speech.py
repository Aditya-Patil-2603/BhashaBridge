from gtts import gTTS
import os
import playsound
import uuid

# Language codes gTTS ke liye
LANGUAGE_CODES = {
    "Hindi": "hi",
    "Marathi": "mr",
    "English": "en"
}

def text_to_speech(text, language="Hindi"):
    lang_code = LANGUAGE_CODES.get(language, "hi")

    # Har baar unique filename banate hain (taaki purani file overwrite/conflict na ho)
    filename = f"output_{uuid.uuid4().hex}.mp3"

    tts = gTTS(text=text, lang=lang_code)
    tts.save(filename)

    print(f"🔊 Bol raha hoon: {text}")
    playsound.playsound(filename)

    # File clean up karo baad mein
    os.remove(filename)


if __name__ == "__main__":
    text_to_speech("नमस्ते, मैं आपकी मदद कर सकता हूं", language="Hindi")