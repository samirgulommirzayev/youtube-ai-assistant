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

# Google tavsiya qilgan rasmiy model kodi
MODEL = "gemini-3.6-flash"  


def ask_ai(system_prompt: str, user_prompt: str, max_tokens: int = 8192) -> str:
    """
    Gemini'ga so'rov yuboradi, matn javobini qaytaradi.
    max_tokens default 8192 qilib o'rnatildi (matn yarimta bo'lib uzilmaydi).
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