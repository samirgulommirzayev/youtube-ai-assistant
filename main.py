import streamlit as st
from core.content_generator import (
    generate_script,
    generate_title_tags_hashtags,
    generate_hooks,
    critique_video,
)
from core.channel_coach import build_growth_roadmap, analyze_channel_gap

st.set_page_config(page_title="YouTube AI Assistant", page_icon="🎬", layout="wide")

st.title("🎬 YouTube AI Assistant")
st.caption("Amerika auditoriyasi uchun kanal boshqaruv yordamchisi")

# Yon menyu (Sidebar)
st.sidebar.header("📌 Menyu")
choice = st.sidebar.radio(
    "Xizmatni tanlang:",
    [
        "1. Ssenariy (script) yaratish",
        "2. Sarlavha + Teg + Hashteg yaratish",
        "3. Hook variantlari yaratish",
        "4. Videomni tahlil qilish",
        "5. 0 dan monetizatsiyaga olib chiqish rejasi",
        "6. Kanal tahlili"
    ]
)

# 1. Ssenariy yaratish
if choice.startswith("1"):
    st.subheader("📝 Ssenariy (script) yaratish")
    niche = st.text_input("Niche (masalan: Roblox story):")
    topic = st.text_input("Video mavzusi/g'oyasi:")
    length = st.number_input("Video uzunligi (soniya):", min_value=5, value=30, step=5)

    if st.button("Ssenariy yaratish", type="primary"):
        if niche and topic:
            with st.spinner("Ssenariy tayyorlanmoqda..."):
                result = generate_script(niche, topic, int(length))
                st.success("Tayyor!")
                st.markdown(result)
        else:
            st.warning("Iltimos, Niche va Mavzuni kiriting!")

# 2. Sarlavha + Teg + Hashteg
elif choice.startswith("2"):
    st.subheader("🏷️ Sarlavha + Teg + Hashteg yaratish")
    niche = st.text_input("Niche:")
    topic = st.text_input("Video mavzusi:")

    if st.button("Generatsiya qilish", type="primary"):
        if niche and topic:
            with st.spinner("Natijalar yaratilmoqda..."):
                result = generate_title_tags_hashtags(niche, topic)
                st.success("Tayyor!")
                st.markdown(result)
        else:
            st.warning("Iltimos, barcha maydonlarni to'ldiring!")

# 3. Hook variantlari
elif choice.startswith("3"):
    st.subheader("🪝 Hook variantlari yaratish")
    niche = st.text_input("Niche:")
    topic = st.text_input("Video mavzusi:")

    if st.button("Hooklarni yaratish", type="primary"):
        if niche and topic:
            with st.spinner("Hooklar oylashtirilmoqda..."):
                result = generate_hooks(niche, topic)
                st.success("Tayyor!")
                st.markdown(result)
        else:
            st.warning("Iltimos, barcha maydonlarni to'ldiring!")

# 4. Video tahlili
elif choice.startswith("4"):
    st.subheader("🔍 Videomni tahlil qilish (nima yetishmayapti)")
    desc = st.text_area("Videongiz haqida yozing (nima bo'layapti, retention, hook):")

    if st.button("Tahlil qilish", type="primary"):
        if desc:
            with st.spinner("Video tahlil qilinmoqda..."):
                result = critique_video(desc)
                st.success("Tahlil yakunlandi!")
                st.markdown(result)
        else:
            st.warning("Iltimos, video haqida ma'lumot kiriting!")

# 5. O'sish rejasi
elif choice.startswith("5"):
    st.subheader("🚀 Kanalni 0 dan monetizatsiyaga olib chiqish rejasi")
    niche = st.text_input("Niche:")
    subs = st.number_input("Hozirgi obunachilar soni:", min_value=0, value=0, step=10)
    status = st.text_area("Hozirgi holat (nechta video, qanday natija):")

    if st.button("Reja tuzish", type="primary"):
        if niche and status:
            with st.spinner("O'sish rejasi tuzilmoqda..."):
                result = build_growth_roadmap(niche, int(subs), status)
                st.success("Reja tayyor!")
                st.markdown(result)
        else:
            st.warning("Iltimos, Niche va Hozirgi holatni kiriting!")

# 6. Kanal tahlili
elif choice.startswith("6"):
    st.subheader("📊 Kanal tahlili (qo'lda ma'lumot kiritib)")
    desc = st.text_area("Kanal haqida ma'lumot (nomi, niche, obunachilar, videolar):")

    if st.button("Kanalni tahlil qilish", type="primary"):
        if desc:
            with st.spinner("Kanal tahlil qilinmoqda..."):
                result = analyze_channel_gap(desc)
                st.success("Tahlil tayyor!")
                st.markdown(result)
        else:
            st.warning("Iltimos, kanal haqida ma'lumot kiriting!")