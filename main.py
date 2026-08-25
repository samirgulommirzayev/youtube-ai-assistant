import streamlit as st

# 1. Barcha Streamlit buyruqlaridan oldin Birinchi bo'lib yozilishi shart!
st.set_page_config(
    page_title="Ulusama AI — YouTube Agent",
    page_icon="🚀",
    layout="wide"
)

# 2. Login tizimi holatini tekshirish
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

PAROL = "ulusama2026"  # Kirish uchun umumiy parol

# 3. Login oynasi
if not st.session_state.logged_in:
    st.title("🔑 Ulusama AI — Tizimga kirish")
    st.write("Dasturdan foydalanish uchun ismingiz va parolni kiriting.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        ism = st.text_input("Ismingizni kiriting:")
        parol_input = st.text_input("Parolni kiriting:", type="password")
        btn = st.button("Kirish")
        
        if btn:
            if parol_input == PAROL and ism.strip() != "":
                st.session_state.logged_in = True
                st.session_state.user_name = ism
                st.rerun()
            elif ism.strip() == "":
                st.error("Iltimos, ismingizni kiriting!")
            else:
                st.error("Parol noto'g'ri!")
    st.stop()

# 4. Premium CSS dizayn
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
    }
    
    h1 {
        background: linear-gradient(90deg, #FF0055 0%, #7A00FF 50%, #00E5FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        font-size: 2.5rem !important;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #161B22;
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #30363D;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF0055, #7A00FF) !important;
        color: #FFFFFF !important;
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FF0055, #7A00FF);
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(122, 0, 255, 0.4);
    }

    section[data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #30363D;
    }
</style>
""", unsafe_allow_html=True)

# 5. Sidebar sozlamalari
st.sidebar.title("🤖 Ulusama AI")
st.sidebar.markdown("**Muallif:** Samir Gulommirzoyev")
st.sidebar.success(f"Xush kelibsiz, **{st.session_state.user_name}**!")

if st.sidebar.button("Chiqish (Logout)"):
    st.session_state.logged_in = False
    st.rerun()

st.sidebar.info("Bu AI agent orqali siz YouTube kanalingizni professional darajada boshqara olasiz.")

# 6. Asosiy sahifa va Tablar
st.title("🚀 Ulusama AI — To'liq YouTube Agent")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💡 Nisha & G'oya", 
    "🎬 YouTube Ssenariy", 
    "🏷️ SEO & Metadata", 
    "🖼️ Logo & Banner", 
    "💬 AI Maslahatchi"
])

with tab1:
    st.header("💡 Nisha va Video G'oyalar Yaratish")
    nisha = st.text_input("Kanal yo'nalishini kiriting (masalan: Texnologiya, O'yin, Ta'lim):")
    if st.button("G'oya Generatsiya Qilish"):
        st.write(f"**{nisha}** yo'nalishi bo'yicha g'oyalar tayyorlanmoqda...")

with tab2:
    st.header("🎬 Professional Video Ssenariy")
    mavzu = st.text_input("Video mavzusini kiriting:")
    if st.button("Ssenariy Yozish"):
        st.write(f"**{mavzu}** bo'yicha ssenariy yaratilmoqda...")

with tab3:
    st.header("🏷️ SEO & Metadata Optimizatsiya")
    video_title = st.text_input("Video nomini kiriting:")
    if st.button("Teg va Tavsiflarni Olish"):
        st.write(f"**{video_title}** uchun SEO teglar tayyorlanmoqda...")

with tab4:
    st.header("🖼️ Logo va Banner Generatori")
    prompt = st.text_input("Dizayn uchun promt kiriting:")
    if st.button("Rasm Yaratish"):
        st.write("Rasm generatsiya qilinmoqda...")

with tab5:
    st.header("💬 AI Maslahatchi bilan Gaplashish")
    st.write("YouTube kanalingizni rivojlantirish bo'yicha erkin muloqot qiling.")
    user_msg = st.text_input("Savolingizni kiriting:", key="chat_input")
    if st.button("Yuborish"):
        st.write(f"**Siz:** {user_msg}")
        st.write("**Ulusama AI:** YouTube algoritmiga ko'ra...")