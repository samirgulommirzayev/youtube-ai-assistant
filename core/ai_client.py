"""
Google Gemini bilan ishlash uchun asosiy wrapper.
Barcha modullar shu orqali AI'ga so'rov yuboradi.
"""
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY .env faylida topilmadi!")

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL = "gemini-3.6-flash"  # tez va sifatli


def ask_ai(system_prompt: str, user_prompt: str, max_tokens: int = 1500) -> str:
    """
    Gemini'ga so'rov yuboradi, matn javobini qaytaradi.
    content_generator.py va channel_coach.py shu funksiyani chaqiradi.
    """
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                max_output_tokens=max_tokens,
            ),
        )
        return response.text.strip()
    except Exception as e:
        return f"[Xatolik yuz berdi]: {e}"


def generate_image(prompt: str, save_path: str = "output_image.png") -> str:
    """
    Logo/banner uchun rasm generatsiyasi (keyinroq ishlatamiz).
    """
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash-image",
            contents=prompt,
        )
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                with open(save_path, "wb") as f:
                    f.write(part.inline_data.data)
                return save_path
        return "[Rasm qaytmadi, promptni tekshiring]"
    except Exception as e:
        return f"[Xatolik yuz berdi]: {e}"