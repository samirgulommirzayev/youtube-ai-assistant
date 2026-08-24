"""
YouTube AI Assistant - Amerika auditoriyasi uchun kanal boshqaruv yordamchisi
Ishga tushirish: python main.py
"""
from rich.console import Console
from rich.panel import Panel
from core.content_generator import (
    generate_script,
    generate_title_tags_hashtags,
    generate_hooks,
    critique_video,
)
from core.channel_coach import build_growth_roadmap, analyze_channel_gap

console = Console()

MENU = """
[bold cyan]YouTube AI Assistant[/bold cyan]

1. Ssenariy (script) yaratish
2. Sarlavha + Teg + Hashteg yaratish
3. Hook variantlari yaratish
4. Videomni tahlil qilish (nima yetishmayapti)
5. Kanalni 0 dan monetizatsiyaga olib chiqish rejasi
6. Kanal tahlili (qo'lda ma'lumot kiritib)
0. Chiqish
"""


def main():
    while True:
        console.print(Panel(MENU))
        choice = input("Tanlang (0-6): ").strip()

        if choice == "1":
            niche = input("Niche (masalan: Roblox story): ")
            topic = input("Video mavzusi/g'oyasi: ")
            length = input("Video uzunligi (soniya, default 30): ") or "30"
            result = generate_script(niche, topic, int(length))
            console.print(Panel(result, title="Ssenariy"))

        elif choice == "2":
            niche = input("Niche: ")
            topic = input("Video mavzusi: ")
            result = generate_title_tags_hashtags(niche, topic)
            console.print(Panel(result, title="Sarlavha / Teg / Hashteg"))

        elif choice == "3":
            niche = input("Niche: ")
            topic = input("Video mavzusi: ")
            result = generate_hooks(niche, topic)
            console.print(Panel(result, title="Hook variantlari"))

        elif choice == "4":
            desc = input("Videongiz haqida yozing (nima bo'layapti, retention, hook): ")
            result = critique_video(desc)
            console.print(Panel(result, title="Video tahlili"))

        elif choice == "5":
            niche = input("Niche: ")
            subs = input("Hozirgi obunachilar soni: ") or "0"
            status = input("Hozirgi holat (nechta video, qanday natija): ")
            result = build_growth_roadmap(niche, int(subs), status)
            console.print(Panel(result, title="O'sish rejasi"))

        elif choice == "6":
            desc = input("Kanal haqida ma'lumot (nomi, niche, obunachilar, videolar): ")
            result = analyze_channel_gap(desc)
            console.print(Panel(result, title="Kanal tahlili"))

        elif choice == "0":
            console.print("Xayr! 👋")
            break

        else:
            console.print("[red]Noto'g'ri tanlov, qaytadan urinib ko'ring[/red]")

        input("\nDavom etish uchun Enter bosing...")


if __name__ == "__main__":
    main()
