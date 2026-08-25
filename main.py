import streamlit as st
from core.ai_client import ask_ai, generate_image
from core.content_generator import YouTubeSsenarist

# --- 0. Konfiguratsiya ---
MUALLIF_ISMI = "Samir Gulommirzoyev"

st.set_page_config(
    page_title=f"Ulusama AI by {MUALLIF_ISMI}",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar (Yon panel) ---
with st.sidebar:
    st.title("🤖 Ulusama AI")
    st.subheader(f"Muallif: {MUALLIF_ISMI}")
    st.markdown("---")
    st.info("Bu AI agent orqali siz YouTube kanalingizni professional darajada boshqara olasiz.")

# --- Asosiy Oyna Sarlavhasi ---
st.title("🚀 Ulusama AI — To'liq YouTube Agent")

# --- 1. Tablarni yaratish ---
tab_scenario, tab_visual, tab_chat = st.tabs([
    "🎬 YouTube Ssenariy", 
    "🖼️ Logo & Banner Generator", 
    "💬 AI Maslahatchi (Chat)"
])

# ==========================================================
# --- Tab 1: YouTube Ssenariy ---
# ==========================================================
with tab_scenario:
    st.header("🎬 Professional Video Ssenariy Yaratish")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Video Ma'lumotlari")
        topic = st.text_input("Video mavzusi:", placeholder="Masalan: Sun'iy intellekt tarixi")
        video_type = st.selectbox("Video turi:", [
            "Ma'rifiy (Educational)", 
            "Yangiliklar (News)", 
            "Texno-sharh (Review)", 
            "Motivatsiya", 
            "Vlog"
        ])
        duration = st.slider("Taxminiy davomiyligi (daqiqa):", 3, 20, 10)
        
        generate_btn = st.button("Ssenariy yaratish", type="primary")
    
    with col2:
        st.subheader("Natija")
        if generate_btn and topic:
            with st.spinner("AI ssenariy ustida ishlamoqda..."):
                ssenarist = YouTubeSsenarist()
                full_prompt = ssenarist.generate_prompt(topic, video_type, duration)
                
                result = ask_ai(
                    system_prompt="Siz tajribali YouTube ssenaristisiz. O'zbek tilida, jozibali, strukturali ssenariy yozib bering.",
                    user_prompt=full_prompt
                )
                
                if "[Matn generatsiyasida xatolik]" not in result:
                    st.success("Ssenariy tayyor!")
                    st.markdown(result)
                else:
                    st.error(result)
        elif generate_btn and not topic:
            st.warning("Iltimos, video mavzusini kiriting.")

# ==========================================================
# --- Tab 2: Logo & Banner Generator ---
# ==========================================================
with tab_visual:
    st.header("🖼️ YouTube Kanalingiz uchun Vizual Kontent")
    st.markdown("YouTube kanalingiz uchun original logo yoki video banner yarating.")
    
    col_v1, col_v2 = st.columns([1, 2])
    
    with col_v1:
        st.subheader("Vizual Sozlamalar")
        visual_type = st.radio("Nima yaratamiz?", ["Kanal Logosi (Square)", "Video Banner (Widescreen 16:9)"])
        
        raw_prompt = st.text_area(
            "Rasm tavsifi (Prompt):", 
            height=150,
            placeholder="Masalan: Kosmosda suzayotgan robot boshi, neon ranglar, futuristik, yuqori sifat, raqamli san'at."
        )
        
        st.caption("Maslahat: Prompt qanchalik batafsil bo'lsa (ranglar, stil, obyektlar), rasm shunchalik yaxshi chiqadi.")
        generate_image_btn = st.button("Vizualni Yaratish", key="gen_img", type="primary")
    
    with col_v2:
        st.subheader("Natija")
        if generate_image_btn and raw_prompt:
            enriched_prompt = ask_ai(
                system_prompt="Siz professional Imagen rasm generatori promptsiz. Foydalanuvchining o'zbek tilidagi qisqa promptini, Imagen 3 modeli tushunadigan, batafsil, stil, yorug'lik va obyektlar kiritilgan Ingliz tilidagi professional promptga aylantiring. Faqat boyitilgan Inglizcha promptni qaytaring.",
                user_prompt=raw_prompt,
                max_tokens=200
            )
            
            st.caption(f"AI tomonidan boyitilgan prompt (Inglizcha): *{enriched_prompt}*")

            with st.spinner("AI rasm chizmoqda... (bu 10-20 soniya olishi mumkin)"):
                image_bytes = generate_image(enriched_prompt)
                
                if image_bytes:
                    st.success("Rasm muvaffaqiyatli yaratildi!")
                    st.image(image_bytes, caption=f"Yaratilgan {visual_type}", use_column_width=True)
                    
                    st.download_button(
                        label="Rasmni yuklab olish",
                        data=image_bytes,
                        file_name=f"ulusama_ai_{visual_type.lower().replace(' ', '_')}.png",
                        mime="image/png"
                    )
                else:
                    st.error("Rasm yaratishda xatolik yuz berdi yoki API rasm qaytarmadi. Promptni soddalashtirib ko'ring.")
        elif generate_image_btn and not raw_prompt:
            st.warning("Iltimos, rasm tavsifini yozing.")

# ==========================================================
# --- Tab 3: AI Maslahatchi (Chat) ---
# ==========================================================
with tab_chat:
    st.header("💬 Ulusama AI bilan Gaplashish")
    st.markdown("YouTube kanalingizni rivojlantirish, g'oyalar, algoritmlar yoki umumiy maslahatlar bo'yicha AI bilan erkin muloqot qiling.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("YouTube haqida nimani bilmoqchisiz?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Ulusama o'ylamoqda..."):
                chat_result = ask_ai(
                    system_prompt=f"Siz Ulusama AI — professional YouTube maslahatchisisiz. Muallif {MUALLIF_ISMI} ga YouTube algoritmlari, kontent yaratish, monetizatsiya va kanal rivojlantirish bo'yicha foydali maslahatlar bering. O'zbek tilida, do'stona va professional tonda gapiring. Agarda savol YouTube'ga aloqador bo'lmasa, do'stona tarzda mavzuga qaytishni so'rang.",
                    user_prompt=prompt,
                    max_tokens=2000
                )
                st.markdown(chat_result)
        
        st.session_state.messages.append({"role": "assistant", "content": chat_result})