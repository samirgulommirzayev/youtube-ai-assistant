"""
Ulusama AI uchun asosiy AI muloqot wrapperi.
Matn va Rasm generatsiyasini boshqaradi.
"""
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY .env faylida topilmadi!")

# GenAI clientni yaratish
client = genai.Client(api_key=GEMINI_API_KEY)

# Modellarni aniqlash
TEXT_MODEL = "gemini-3.6-flash"  # Matn va chat uchun
IMAGE_MODEL = "imagen-3.0-generate-002"  # Rasm/Logo uchun

# --- 1. Matn bilan ishlash funksiyasi (Hozirgi ssenariy va Chat uchun) ---
def ask_ai(system_prompt: str, user_prompt: str, max_tokens: int = 8192) -> str:
    """
    Gemini'ga so'rov yuboradi, matn javobini qaytaradi.
    max_tokens default 8192 (javob to'liq chiqishi uchun).
    """
    try:
        response = client.models.generate_content(
            model=TEXT_MODEL,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                max_output_tokens=max_tokens,
            ),
        )
        return response.text.strip()
    except Exception as e:
        return f"[Matn generatsiyasida xatolik]: {e}"

# --- 2. Rasm bilan ishlash funksiyasi (Logo va Banner uchun) ---
def generate_image(prompt: str) -> BytesIO:
    """
    Kiritilgan prompt asosida Imagen 3 yordamida rasm yaratadi.
    Chiqishda Streamlit ko'rsata oladigan BytesIO obyektini qaytaradi.
    """
    try:
        response = client.models.generate_images(
            model=IMAGE_MODEL,
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1, # 1 ta rasm kifoya
                safety_filter_level="BLOCK_MEDIUM_AND_ABOVE"
            )
        )
        
        if response.generated_images:
            image_data = response.generated_images[0].image_bytes
            return BytesIO(image_data)
        else:
            return None
            
    except Exception as e:
        # Xatolik bo'lsa, konsolga yozadi va None qaytaradi
        print(f"[Rasm generatsiyasida xatolik]: {e}")
        return None