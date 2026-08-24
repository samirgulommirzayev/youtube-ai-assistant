"""
YouTube AI Assistant - Veb-sayt versiyasi (Streamlit)
Ishga tushirish: streamlit run app.py
"""
import streamlit as st
from core.content_generator import (
    generate_script,
    generate_title_tags_hashtags,
    generate_hooks,
    critique_video,
)
from core.channel_coach import build_growth_roadmap, analyze_channel_gap

# ----- Sahifa sozlamalari -----
st.set_page_config(
    page_title="YouTube AI Assistant",
    page_icon="🎬",
    layout="centered",
)

st.title("🎬 YouTube AI Assistant")
st.caption("Amerika auditoriyasi uchun kanal boshqaruv yordamchisi")

# ----- Chap panel: bo'lim tanlash -----
st.sidebar.header("Bo'lim tanlang")
choice = st.sidebar.radio(
    "Nima qilmoqchisiz?",
    [
        "1. Ssenariy yaratish",
        "2. Sarlavha + Teg + Hashteg",
        "3. Hook variantlari",
        "4. Video tahlili",
        "5. O'sish rejasi (0 dan monetizatsiyaga)",
        "6. Kanal tahlili",
    ],
)

st.divider()

# ----- Har bir bo'lim uchun forma -----

if choice == "1. Ssenariy yaratish":
    st.subheader("📝 Ssenariy yaratish")
    niche = st.text_input("Niche (masalan: Roblox story)")
    topic = st.text_input("Video mavzusi/g'oyasi")
    length = st.number_input("Video uzunligi (soniya)", min_value=5, max_value=600, value=30)

    if st.button("Ssenariy yaratish", type="primary"):
        if not niche or not topic:
            st.warning("Iltimos, niche va mavzuni to'ldiring.")
        else:
            with st.spinner("Yozilmoqda..."):
                result = generate_script(niche, topic, int(length))
            st.success("Tayyor!")
            st.markdown(result)

elif choice == "2. Sarlavha + Teg + Hashteg":
    st.subheader("🏷️ Sarlavha, Teg va Hashteg")
    niche = st.text_input("Niche")
    topic = st.text_input("Video mavzusi")

    if st.button("Yaratish", type="primary"):
        if not niche or not topic:
            st.warning("Iltimos, niche va mavzuni to'ldiring.")
        else:
            with st.spinner("Yozilmoqda..."):
                result = generate_title_tags_hashtags(niche, topic)
            st.success("Tayyor!")
            st.markdown(result)

elif choice == "3. Hook variantlari":
    st.subheader("🎣 Hook variantlari")
    niche = st.text_input("Niche")
    topic = st.text_input("Video mavzusi")

    if st.button("Hook yaratish", type="primary"):
        if not niche or not topic:
            st.warning("Iltimos, niche va mavzuni to'ldiring.")
        else:
            with st.spinner("Yozilmoqda..."):
                result = generate_hooks(niche, topic)
            st.success("Tayyor!")
            st.markdown(result)

elif choice == "4. Video tahlili":
    st.subheader("🔍 Videoingizni tahlil qilish")
    desc = st.text_area(
        "Videongiz haqida yozing (nima bo'layapti, retention, hook)",
        height=150,
    )

    if st.button("Tahlil qilish", type="primary"):
        if not desc:
            st.warning("Iltimos, video haqida ma'lumot yozing.")
        else:
            with st.spinner("Tahlil qilinmoqda..."):
                result = critique_video(desc)
            st.success("Tayyor!")
            st.markdown(result)

elif choice == "5. O'sish rejasi (0 dan monetizatsiyaga)":
    st.subheader("🚀 O'sish rejasi")
    niche = st.text_input("Niche")
    subs = st.number_input("Hozirgi obunachilar soni", min_value=0, value=0)
    status = st.text_area("Hozirgi holat (nechta video, qanday natija)", height=100)

    if st.button("Reja tuzish", type="primary"):
        if not niche or not status:
            st.warning("Iltimos, barcha maydonlarni to'ldiring.")
        else:
            with st.spinner("Reja tuzilmoqda..."):
                result = build_growth_roadmap(niche, int(subs), status)
            st.success("Tayyor!")
            st.markdown(result)

elif choice == "6. Kanal tahlili":
    st.subheader("📊 Kanal tahlili")
    desc = st.text_area(
        "Kanal haqida ma'lumot (nomi, niche, obunachilar, videolar)",
        height=150,
    )

    if st.button("Tahlil qilish", type="primary"):
        if not desc:
            st.warning("Iltimos, kanal haqida ma'lumot yozing.")
        else:
            with st.spinner("Tahlil qilinmoqda..."):
                result = analyze_channel_gap(desc)
            st.success("Tayyor!")
            st.markdown(result)
