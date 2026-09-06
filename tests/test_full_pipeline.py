import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from voice.speech_to_text import speech_to_text
from voice.text_to_speech import text_to_speech
from language.language_detector import detect_language
from language.translator import translate_text

if __name__ == "__main__":
    # Step A: Jis language mein tum bologe, wo yahan set karo
    spoken_language = "Hindi"   # "Hindi" / "Marathi" / "English"

    # Step B: Jis language mein translate + bolna hai, wo yahan set karo
    target_language = "Marathi"

    # 1) Awaaz ko text mein badlo
    text = speech_to_text(language=spoken_language)

    if text:
        # 2) Detect karo kaunsi language hai (cross-check ke liye)
        detected = detect_language(text)
        print(f"🔍 Detected language: {detected}")

        # 3) Translate karo target language mein
        translated = translate_text(text, target_language=target_language)
        print(f"🌐 Translated ({target_language}): {translated}")

        # 4) Translated text ko bolo
        text_to_speech(translated, language=target_language)
    else:
        print("Kuch samajh nahi aaya, dobara try karo.")