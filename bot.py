import os
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = os.environ.get("BOT_TOKEN") 
KARTA_RAQAMI = "8600 0000 0000 0000"
KARTA_EGA_ISMI = "SAMIR G."
TOLOV_SUMMASI = "10 000 so'm"
SAYT_LINK = "https://ulusama-ai.onrender.com"
SAYT_PAROL = "ulusama2026"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

class Registration(StatesGroup):
    waiting_for_name = State()
    waiting_for_check = State()

@dp.message(CommandStart())
async def start_cmd(message: types.Message, state: FSMContext):
    await message.answer(
        "👋 **Xush kelibsiz!**\n\n"
        "Ulusama AI xizmatidan foydalanish uchun, iltimos, **ismingizni** kiriting:"
    )
    await state.set_state(Registration.waiting_for_name)

@dp.message(Registration.waiting_for_name, F.text)
async def process_name(message: types.Message, state: FSMContext):
    user_name = message.text.strip()
    await state.update_data(user_name=user_name)
    
    text = (
        f"Rahmat, **{user_name}**!\n\n"
        f"📌 **To'lov ma'lumotlari:**\n"
        f"🔹 **Karta raqami:** `{KARTA_RAQAMI}`\n"
        f"🔹 **Karta egasi:** {KARTA_EGA_ISMI}\n"
        f"💰 **To'lov summasi:** {TOLOV_SUMMASI}\n\n"
        f"📲 **To'lov usullari:** Click, Payme, Uzum Bank orqali to'lashingiz mumkin.\n\n"
        f"⚠️ **To'lovni amalga oshirgach, to'lov cheki (skrinshot/rasm)ni shu chatga yuboring!**"
    )
    await message.answer(text, parse_mode="Markdown")
    await state.set_state(Registration.waiting_for_check)

@dp.message(Registration.waiting_for_check, F.photo)
async def process_check(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_name = user_data.get("user_name", "Foydalanuvchi")
    
    await message.answer("🔄 **To'lov cheki qabul qilindi! Tekshirilmoqda...**")
    await asyncio.sleep(2)
    
    success_text = (
        f"🎉 **To'lov muvaffaqiyatli tasdiqlandi, {user_name}!**\n\n"
        f"🚀 Saytga kirish uchun ma'lumotlar:\n\n"
        f"🌐 **Sayt havolasi:** {SAYT_LINK}\n"
        f"👤 **Ismingiz:** {user_name}\n"
        f"🔑 **Parol:** `{SAYT_PAROL}`\n\n"
        f"Saytga kirib, ismingiz va parolni kiritib foydalanishingiz mumkin!"
    )
    await message.answer(success_text, parse_mode="Markdown")
    await state.clear()

@dp.message(Registration.waiting_for_check)
async def process_check_invalid(message: types.Message):
    await message.answer("⚠️ Iltimos, to'lov amalga oshirilgani haqidagi **chek rasmini (skrinshot)** yuboring!")

async def handle(request):
    return web.Response(text="Bot Active")

async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    
    # Render avtomatik ajratadigan PORTni olish
    port = int(os.environ.get("PORT", 10000))
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    
    print(f"Web server started on port {port}")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
