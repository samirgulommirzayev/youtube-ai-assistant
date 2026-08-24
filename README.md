# YouTube AI Assistant

Amerika auditoriyasi uchun YouTube kanal boshqaruv yordamchisi.

## 1-QADAM: O'rnatish (VS Code'da)

```bash
# 1. Papkani VS Code'da oching
# 2. Terminalda virtual environment yarating:
python -m venv venv

# 3. Faollashtiring:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Kutubxonalarni o'rnating:
pip install -r requirements.txt
```

## 2-QADAM: API kalitni sozlash

1. `.env.example` faylini nusxalab `.env` deb nomlang
2. https://console.anthropic.com ga kirib API kalit oling
3. `.env` faylga kalitingizni qo'ying:
   ```
   ANTHROPIC_API_KEY=sk-ant-sizning-kalitingiz
   ```

## 3-QADAM: Ishga tushirish

```bash
python main.py
```

Menyudan kerakli funksiyani tanlang (raqam kiritib Enter bosing).

## Hozircha ishlaydigan funksiyalar

| # | Funksiya | Holati |
|---|----------|--------|
| 1 | Ssenariy generatori | ✅ Ishlaydi |
| 2 | Sarlavha/Teg/Hashteg | ✅ Ishlaydi |
| 3 | Hook generatori | ✅ Ishlaydi |
| 4 | Video tahlili (qo'lda kiritilgan ma'lumot asosida) | ✅ Ishlaydi |
| 5 | O'sish/monetizatsiya rejasi | ✅ Ishlaydi |
| 6 | Kanal tahlili (qo'lda kiritilgan ma'lumot asosida) | ✅ Ishlaydi |

## Hali qo'shilmagan (keyingi bosqichlar)

Bular texnik jihatdan boshqacha yondashuv talab qiladi, shuning uchun alohida qo'shiladi:

- **Logo/Banner generatori** — rasm generatsiya API kerak (masalan OpenAI DALL-E
  yoki Google Imagen). Claude matn yaratadi, rasm yaratmaydi.
- **Avtomatik kanal analizi (real vaqtda)** — hozir siz ma'lumotni qo'lda
  kiritasiz (6-bo'lim). To'liq avtomatlashtirish uchun YouTube Data API +
  OAuth ulanishi kerak (bu Google Cloud Console'da alohida sozlash talab qiladi).
- **Yuklash vaqtini tavsiya qilish** — bu ham YouTube Analytics API orqali
  kanalning haqiqiy audience faollik grafigini olishni talab qiladi.

Ayting, keyingi qaysi qismni qo'shishimni xohlaysiz — men shu loyihaga
qo'shib beraman.

## Loyiha tuzilishi

```
youtube-ai-assistant/
├── main.py                    # Asosiy dastur (CLI menyu)
├── core/
│   ├── ai_client.py            # Claude API wrapper
│   ├── content_generator.py    # Skript/sarlavha/teg/hook
│   └── channel_coach.py        # O'sish rejasi/kanal tahlili
├── requirements.txt
├── .env.example
└── .env                        # (o'zingiz yaratasiz, API kalit shu yerda)
```
