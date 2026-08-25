import streamlit as st
from core.ai_client import ask_ai, generate_image

# --- 0. Konfiguratsiya ---
MUALLIF_ISMI = "Samir Gulommirzoyev"

st.set_page_config
st.markdown("""
<style>
    /* Asosiy fon va shriftlar */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Sarlavha uchun gradient va neon effekt */
    h1 {
        background: linear-gradient(90deg, #FF0055 0%, #7A00FF 50%, #00E5FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        font-size: 2.8rem !important;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Tab tugmalarini stilizatsiya qilish */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #161B22;
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #30363D;
    }

    .stTabs [data-baseweb="tab"] {
        height: 45px;
        border-radius: 8px;
        color: #8B949E;
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF0055, #7A00FF) !important;
        color: #FFFFFF !important;
    }
    
    /* Input va Textarea oynalari */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #161B22 !important;
        color: #F0F6FC !important;
        border-radius: 10px !important;
        border: 1px solid #30363D !important;
    }

    /* Barcha tugmalar uchun premium stil */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FF0055, #7A00FF);
        color: white;
        font-weight: bold;
        border: none;
        padding: 12px 24px;
        border-radius: 10px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 0, 85, 0.3);
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(122, 0, 255, 0.5);
    }

    /* Sidebar dizayni */
    section[data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #30363D;
    }
</style>
""", unsafe_allow_html=True) 
(
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

# --- 1. Tablarni yaratish (5 ta bo'lim) ---
tab_niche, tab_scenario, tab_seo, tab_visual, tab_chat = st.tabs([
    "💡 Nisha & G'oya Tanlash",
    "🎬 YouTube Ssenariy", 
    "🏷️ SEO & Metadata",
    "🖼️ Logo & Banner Generator", 
    "💬 AI Maslahatchi (Chat)"
])

# ==========================================================
# --- Tab 1: Nisha & G'oya Tanlash ---
# ==========================================================
with tab_niche:
    st.header("💡 Qiziqishingizga mos YouTube Yo'nalishini Topish")
    st.markdown("Qiziqishlaringiz va imkoniyatlaringizni kiriting — AI sizga eng mos yo'nalish va video g'oyalarini taklif qiladi.")
    
    col_n1, col_n2 = st.columns([1, 2])
    
    with col_n1:
        st.subheader("Siz haqida")
        interests = st.text_area(
            "Qiziqishlaringiz va sevimli mashg'ulotlaringiz:", 
            placeholder="Masalan: Texnika, o'yinlar, kitob o'qish, futbol, montaj qilish, chet tillari...",
            key="n_interests"
        )
        skills = st.text_input(
            "Mavjud ko'nikmalaringiz (ixtiyoriy):", 
            placeholder="Masalan: Kamera qarshisida erkin gapirish, videoni tez montaj qilish...",
            key="n_skills"
        )
        time_available = st.selectbox(
            "Haftasiga ajrata oladigan vaqtingiz:",
            ["1-3 soat", "4-7 soat", "10+ soat (To'liq stavka)"],
            key="n_time"
        )
        
        find_niche_btn = st.button("Yo'nalish va G'oyalarni Topish", type="primary", key="n_btn")
        
    with col_n2:
        st.subheader("AI Tavsiyalari")
        if find_niche_btn and interests:
            with st.spinner("Qiziqishlaringiz tahlil qilinmoqda..."):
                niche_prompt = f"""
                Foydalanuvchi qiziqishlari: {interests}
                Ko'nikmalari: {skills}
                Ajrata oladigan vaqti: {time_available}
                
                Quyidagi strukturada tavsiya bering:
                1. 🎯 **3 ta eng mos YouTube Yo'nalishi (Nisha)** va ularning sababi.
                2. 💡 **Har bir yo'nalish uchun 3 tadan top video g'oyasi (Jami 9 ta g'oya)**.
                3. 📈 **Ushbu yo'nalishda auditoriyani jalb qilish bo'yicha qisqa maslahat**.
                """
                
                niche_result = ask_ai(
                    system_prompt="Siz YouTube kanal strategi va ekspertisiz. O'zbek tilida aniq, tushunarli va motivatsion javob bering.",
                    user_prompt=niche_prompt
                )
                
                if "[Matn generatsiyasida xatolik]" not in niche_result:
                    st.success("Tavsiyalar tayyor!")
                    st.markdown(niche_result)
                else:
                    st.error(niche_result)
        elif find_niche_btn and not interests:
            st.warning("Iltimos, kamida qiziqishlaringizni kiriting.")

# ==========================================================
# --- Tab 2: YouTube Ssenariy ---
# ==========================================================
with tab_scenario:
    st.header("🎬 Professional Video Ssenariy Yaratish")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Video Ma'lumotlari")
        topic = st.text_input("Video mavzusi:", placeholder="Masalan: Sun'iy intellekt tarixi", key="sc_topic")
        video_type = st.selectbox("Video turi:", [
            "Ma'rifiy (Educational)", 
            "Yangiliklar (News)", 
            "Texno-sharh (Review)", 
            "Motivatsiya", 
            "Vlog"
        ], key="sc_type")
        duration = st.slider("Taxminiy davomiyligi (daqiqa):", 3, 20, 10, key="sc_dur")
        
        generate_btn = st.button("Ssenariy yaratish", type="primary", key="sc_btn")
    
    with col2:
        st.subheader("Natija")
        if generate_btn and topic:
            with st.spinner("AI ssenariy ustida ishlamoqda..."):
                prompt = f"Mavzu: {topic}\nVideo turi: {video_type}\nDavomiyligi: {duration} daqiqa.\n\nUshbu video uchun batafsil YouTube ssenariysini tayyorlab ber."
                
                result = ask_ai(
                    system_prompt="Siz tajribali YouTube ssenaristisiz. O'zbek tilida, jozibali, strukturali ssenariy yozib bering.",
                    user_prompt=prompt
                )
                
                if "[Matn generatsiyasida xatolik]" not in result:
                    st.success("Ssenariy tayyor!")
                    st.markdown(result)
                else:
                    st.error(result)
        elif generate_btn and not topic:
            st.warning("Iltimos, video mavzusini kiriting.")

# ==========================================================
# --- Tab 3: SEO & Metadata ---
# ==========================================================
with tab_seo:
    st.header("🏷️ YouTube SEO va Optimizatsiya")
    st.markdown("Videongiz ko'proq ko'rilishi uchun optimal sarlavha, tavsif, teglar va xeshteglar yarating.")
    
    col_seo1, col_seo2 = st.columns([1, 2])
    
    with col_seo1:
        st.subheader("Video haqida")
        seo_topic = st.text_input("Video mavzusi yoki qisqacha mazmuni:", placeholder="Masalan: Python dasturlashni 0 dan o'rganish", key="seo_topic")
        seo_btn = st.button("SEO elementlarini yaratish", type="primary", key="seo_btn")
        
    with col_seo2:
        st.subheader("SEO Natijalari")
        if seo_btn and seo_topic:
            with st.spinner("SEO optimizatsiya tayyorlanmoqda..."):
                seo_prompt = f"""
                Mavzu: {seo_topic}
                
                Quyidagi formatda YouTube video uchun optimizatsiya qilingan ma'lumotlarni chiqarib ber:
                1. 🎯 **5 ta CTRi yuqori Sarlavha (Title Variantlari)**
                2. 📝 **Professional Video Tavsifi (Description)**
                3. 🏷️ **Teglar (Tags)** - vergul bilan ajratilgan holda
                4. 📌 **Top 5 Xeshteglar (#Hashtags)**
                """
                
                seo_result = ask_ai(
                    system_prompt="Siz YouTube SEO bo'yicha mutaxassisiz. O'zbek tilida video algoritmlarga mos SEO matnlarni tayyorlang.",
                    user_prompt=seo_prompt
                )
                
                if "[Matn generatsiyasida xatolik]" not in seo_result:
                    st.success("SEO paket tayyor!")
                    st.markdown(seo_result)
                else:
                    st.error(seo_result)
        elif seo_btn and not seo_topic:
            st.warning("Iltimos, video mavzusini kiriting.")

# ==========================================================
# --- Tab 4: Logo & Banner Generator ---
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
# --- Tab 5: AI Maslahatchi (Chat) ---
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
