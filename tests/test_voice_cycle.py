import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from voice.speech_to_text import speech_to_text
from voice.text_to_speech import text_to_speech

if __name__ == "__main__":
    # Abhi ke liye yahan manually language change karke test karo
    selected_language = "Hindi"   # "Hindi" / "Marathi" / "English" try kar sakte ho

    text = speech_to_text(language=selected_language)

    if text:
        print(f"\n➡️ Ab wapas bol raha hoon isi text ko: '{text}' ({selected_language})")
        text_to_speech(text, language=selected_language)
    else:
        print("Kuch samajh nahi aaya, dobara try karo.")