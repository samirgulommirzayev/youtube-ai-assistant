import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Ulusama AI — YouTube Agent",
    page_icon="🚀",
    layout="wide"
)

# 2. Login Tizimi
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

PAROL = "ulusama2026"

if not st.session_state.logged_in:
    st.title("🔑 Ulusama AI — Tizimga kirish")
    st.write("Dasturdan foydalanish uchun ismingiz va parolni kiriting.")
    
    col1, _ = st.columns([1, 1])
    with col1:
        ism = st.text_input("Ismingizni kiriting:")
        parol_input = st.text_input("Parolni kiriting:", type="password")
        if st.button("Kirish"):
            if parol_input == PAROL and ism.strip() != "":
                st.session_state.logged_in = True
                st.session_state.user_name = ism
                st.rerun()
            elif ism.strip() == "":
                st.error("Iltimos, ismingizni kiriting!")
            else:
                st.error("Parol noto'g'ri!")
    st.stop()

# 3. CSS Stilizatsiya
st.markdown("""
<style>
    .stApp { background-color: #0E1117; }
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

# 4. Sidebar
st.sidebar.title("🤖 Ulusama AI")
st.sidebar.markdown("**Muallif:** Samir Gulommirzoyev")
st.sidebar.success(f"Xush kelibsiz, **{st.session_state.user_name}**!")

if st.sidebar.button("Chiqish (Logout)"):
    st.session_state.logged_in = False
    st.rerun()

st.sidebar.info("Bu AI agent orqali siz YouTube kanalingizni professional darajada boshqara olasiz.")

# 5. Asosiy Interfeys va Tablar
st.title("🚀 Ulusama AI — To'liq YouTube Agent")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💡 Nisha & G'oya", 
    "🎬 YouTube Ssenariy", 
    "🏷️ SEO & Metadata", 
    "🖼️ Logo & Banner", 
    "📈 AI Strateg"
])

# 1-TAB: Nisha & G'oya
with tab1:
    st.header("💡 Nisha va Video G'oyalar Yaratish")
    qiziqish = st.text_input("Qaysi sohalarga qiziqasiz? (Majburiy):", placeholder="masalan: IT, futbol, pazandachilik...")
    vaqt = st.selectbox(
        "Haftasiga YouTube uchun qancha vaqt ajrata olasiz?",
        ["2-3 soat (Yengil / Shorts)", "3-10 soat (Standard Videolar)", "10+ soat (Professional / Chuqur Videolar)"]
    )
    talant = st.text_input("Qanday talantingiz bor? (Ixtiyoriy):", placeholder="masalan: Chiroyli gapirish, montaj, rasm chizish...")
    
    if st.button("G'oyalarni Generatsiya Qilish", key="tab1_btn"):
        if not qiziqish.strip():
            st.warning("Iltimos, avval qiziqishlaringizni kiriting!")
        else:
            st.success("Tahlil yakunlandi!")
            st.markdown(f"""
            ### 🎯 Siz uchun tavsiya etilgan strategiya:
            * **Qiziqish:** {qiziqish}
            * **Ajratilgan vaqt:** {vaqt}
            * **Talant:** {talant if talant.strip() else 'Kiritilmadi'}

            **💡 Tavsiya etiladigan video yo'nalishlari:**
            1. **Format:** {qiziqish} sohasida eng ko'p beriladigan savollarga javob beruvchi Shorts va haftalik blog.
            2. **Konsept:** {talant if talant.strip() else qiziqish} mahoratidan foydalanib amaliy darsliklar zanjirini yaratish.
            """)

# 2-TAB: YouTube Ssenariy
with tab2:
    st.header("🎬 Professional Video Ssenariy")
    mavzu = st.text_input("Video mavzusi:", placeholder="masalan: Sun'iy intellekt kelajakda ish o'rinlarini egallaydimi?")
    nisha_2 = st.text_input("Nishasi qanaqa (yo'nalishi)?", placeholder="masalan: Texnologiya")
    davomiylik = st.select_slider(
        "Qancha vaqtga mos ssenariy bo'lishi kerak?",
        options=["60 soniya (Shorts)", "3-5 daqiqa", "8-10 daqiqa", "15+ daqiqa"]
    )
    
    if st.button("Ssenariy Yozish", key="tab2_btn"):
        if not mavzu.strip() or not nisha_2.strip():
            st.warning("Iltimos, video mavzusi va nishasini kiriting!")
        else:
            st.success(f"{davomiylik}lik video uchun ssenariy strukturasi:")
            st.markdown(f"""
            **Mavzu:** {mavzu} | **Nisha:** {nisha_2}
            
            ---
            * **[00:00 - 00:15] HOOK (E'tiborni tortish):** "Bilarmidingiz? ..." iborasi bilan tomoshabinni ushlab qolish.
            * **[00:15 - 01:00] KIRISH:** Mavzuning nega muhimligi va videoda nimalar ko'rsatilishi haqida qisqacha.
            * **[ASOSIY QISM]:** {mavzu} bo'yicha 3 ta eng muhim fakt va misollar tahlili.
            * **[CHAQIRIQLAR (CTA)]:** Kanalga obuna bo'lish va izoh qoldirishni so'rash.
            """)

# 3-TAB: SEO & Metadata
with tab3:
    st.header("🏷️ SEO & Metadata Optimizatsiya")
    video_nomi = st.text_input("Video nomini kiriting:", placeholder="masalan: 10 ta eng yaxshi AI dasturlar")
    nisha_3 = st.text_input("Yo'nalishini (nishasini) kiriting:", placeholder="masalan: Texnologiya")
    
    if st.button("SEO Tag va Tavsiflarni Olish", key="tab3_btn"):
        if not video_nomi.strip() or not nisha_3.strip():
            st.warning("Iltimos, video nomi va yo'nalishini kiriting!")
        else:
            st.success("SEO Ma'lumotlar Tayyor!")
            st.markdown(f"""
            **📌 Optimal Video Nomi:** 
            `{video_nomi} | Top Qurollar ({nisha_3})`

            **🏷️ Top Kalit So'zlar (Tags):**
            `{video_nomi}, {nisha_3}, uzbek youtube, foydali ai, texnologiyalar, yangi dasturlar`

            **📝 Video Tavsifi (Description):**
            Ushbu videoda biz {nisha_3} sohasidagi eng dolzarb ma'lumotlar va {video_nomi} haqida batafsil gaplashamiz. Videoni oxirigacha tomosha qiling va o'z fikringizni izohda qoldiring!
            """)

# 4-TAB: Logo & Banner
with tab4:
    st.header("🖼️ Logo va Banner Generatori")
    kanal_nomi = st.text_input("Kanal nomini kiriting:", placeholder="masalan: Ulusama Tech")
    nisha_4 = st.text_input("Kanal yo'nalishini kiriting:", placeholder="masalan: O'yin / Gaming")
    
    if st.button("Dizayn Promptlarini Yaratish", key="tab4_btn"):
        if not kanal_nomi.strip() or not nisha_4.strip():
            st.warning("Iltimos, kanal nomi va yo'nalishini kiriting!")
        else:
            st.success("Midjourney / DALL-E uchun tayyor promptlar:")
            st.code(f"Logo Prompt: A modern vector logo for YouTube channel '{kanal_nomi}', {nisha_4} theme, neon colors, minimalist design, dark background, 8k --v 6.0", language="text")
            st.code(f"Banner Prompt: Futuristic YouTube channel banner for '{kanal_nomi}', {nisha_4} style, high quality render, 16:9 ratio, sleek dynamic elements --ar 16:9", language="text")

# 5-TAB: AI Strateg
with tab5:
    st.header("📈 Ulusama AI — YouTube O'sish Analitigi & Chat")
    st.write("Kanalingiz ko'rishlar sonini va obunachilarini oshirish bo'yicha aqlli maslahatchi.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        sub_count = st.number_input("Hozirgi obunachilar soni:", min_value=0, value=100)
    with col_b:
        goal = st.selectbox("Asosiy maqsadingiz:", ["Monetizatsiya yoqish (1000 sub)", "Tezkor ko'rishlar (Shorts)", "Brend yaratish"])
        
    if st.button("O'sish Strategiyasini Ishlab Chiqish", key="tab5_btn"):
        st.success("AI Tahlil berdi:")
        st.markdown(f"""
        ### 🚀 Sizning bosqichma-bosqich rejangiz:
        * **Hozirgi holat:** {sub_count} ta obunachi.
        * **Maqsad:** {goal}.
        
        **Tavsiya etiladigan kontent nisbati:**
        * **70% Shorts:** Auditoriya va yangi obunachilarni jalb qilish uchun.
        * **30% Uzoq videolar:** Tomosha vaqtini (Watch time) yig'ish va monetizatsiya ochish uchun.
        """)
