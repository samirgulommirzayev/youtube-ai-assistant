import os
import urllib.parse
import streamlit as st
from google import genai
from openai import OpenAI

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

# 3. API Klientlarini sozlash
gemini_key = os.environ.get("GEMINI_API_KEY")
openrouter_key = os.environ.get("OPENROUTER_API_KEY")

gemini_client = genai.Client(api_key=gemini_key) if gemini_key else None
openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openrouter_key
) if openrouter_key else None

# 4. CSS Stilizatsiya
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

# 5. Sidebar & Model Tanlash
st.sidebar.title("🤖 Ulusama AI")
st.sidebar.markdown("**Muallif:** Samir Gulommirzoyev")
st.sidebar.success(f"Xush kelibsiz, **{st.session_state.user_name}**!")

selected_model = st.sidebar.selectbox(
    "🧠 AI Modelini tanlang:",
    options=[
        "Gemini 3.6 Flash (Google)",
        "ChatGPT (GPT-4o Mini)",
        "Claude 3.5 Sonnet (Anthropic)"
    ]
)

if st.sidebar.button("Chiqish (Logout)"):
    st.session_state.logged_in = False
    st.rerun()

# AI ga matnli so'rov yuborish funksiyasi
def ask_ai(prompt):
    if "Gemini" in selected_model:
        if not gemini_client:
            return "❌ GEMINI_API_KEY topilmadi!"
        res = gemini_client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return res.text
    else:
        if not openrouter_client:
            return "❌ OPENROUTER_API_KEY topilmadi!"
        
        model_name = "openai/gpt-4o-mini" if "ChatGPT" in selected_model else "anthropic/claude-3.5-sonnet"
        
        res = openrouter_client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content

# 6. Asosiy Interfeys va Tablar
st.title("🚀 Ulusama AI — To'liq YouTube Agent")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💡 Nisha & G'oya", 
    "🎬 YouTube Ssenariy", 
    "🏷️ SEO & Metadata", 
    "🖼️ Logo & Banner Generator", 
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
    talant = st.text_input("Qanday talantingiz bor? (Ixtiyoriy):", placeholder="masalan: Chiroyli gapirish, montaj...")
    
    if st.button("G'oyalarni Generatsiya Qilish", key="tab1_btn"):
        if not qiziqish.strip():
            st.warning("Iltimos, avval qiziqishlaringizni kiriting!")
        else:
            with st.spinner(f"{selected_model} tahlil qilmoqda..."):
                prompt = f"""
                Foydalanuvchi ma'lumotlari:
                - Qiziqqan sohasi: {qiziqish}
                - Ajrata oladigan vaqti: {vaqt}
                - Qobiliyati/Talanti: {talant if talant.strip() else 'Kiritilmadi'}
                
                Ushbu foydalanuvchi uchun YouTube'da muvaffaqiyat qozonishi mumkin bo'lgan 3 ta aniq video nishasi va 5 ta qiziqarli video g'oyasini o'zbek tilida ber.
                """
                javob = ask_ai(prompt)
                st.success("Tahlil yakunlandi!")
                st.markdown(javob)

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
            with st.spinner(f"{selected_model} ssenariy yozmoqda..."):
                prompt = f"""
                Mavzu: {mavzu}
                Nisha: {nisha_2}
                Vaqt: {davomiylik}
                
                Ushbu video uchun professional YouTube ssenariysini tayyorlab ber (O'zbek tilida). 
                Struktura:
                - Hook (Dastlabki 10 soniya)
                - Kirish
                - Asosiy qism (Faktlar va tavsiyalar)
                - Call to Action (Obuna bo'lishga chaqiriq)
                """
                javob = ask_ai(prompt)
                st.success("Ssenariy tayyor!")
                st.markdown(javob)

# 3-TAB: SEO & Metadata
with tab3:
    st.header("🏷️ SEO & Metadata Optimizatsiya")
    video_nomi = st.text_input("Video nomini kiriting:", placeholder="masalan: 10 ta eng yaxshi AI dasturlar")
    nisha_3 = st.text_input("Yo'nalishini (nishasini) kiriting:", placeholder="masalan: Texnologiya")
    
    if st.button("SEO Tag va Tavsiflarni Olish", key="tab3_btn"):
        if not video_nomi.strip() or not nisha_3.strip():
            st.warning("Iltimos, video nomi va yo'nalishini kiriting!")
        else:
            with st.spinner(f"{selected_model} SEO tayyorlamoqda..."):
                prompt = f"""
                Video Nomi: {video_nomi}
                Nisha: {nisha_3}
                
                Ushbu video uchun:
                1. 3 ta eng jozibador YouTube sarlavha variantlari.
                2. SEO kalit so'zlar (Tags) ro'yxati (vergul bilan ajratilgan).
                3. Algoritmga mos YouTube Description (Tavsif) matni.
                """
                javob = ask_ai(prompt)
                st.success("SEO Ma'lumotlar Tayyor!")
                st.markdown(javob)

# 4-TAB: Logo & Banner (Rasm Generatsiyasi bilan)
with tab4:
    st.header("🖼️ AI Logo va Banner Generatori")
    kanal_nomi = st.text_input("Kanal nomini kiriting:", placeholder="masalan: Ulusama Tech")
    nisha_4 = st.text_input("Kanal yo'nalishini kiriting:", placeholder="masalan: Gaming / Roblox")
    
    if st.button("Logo va Banner Yaratish", key="tab4_btn"):
        if not kanal_nomi.strip() or not nisha_4.strip():
            st.warning("Iltimos, kanal nomi va yo'nalishini kiriting!")
        else:
            with st.spinner("AI Logo va Banner rasmlarini generatsiya qilmoqda..."):
                import random
                seed_val = random.randint(1, 99999)
                
                # Begona belgilardan tozalangan oddiy prompt
                clean_name = kanal_nomi.strip().replace(" ", "_")
                clean_nisha = nisha_4.strip().replace(" ", "_")
                
                logo_prompt = f"vector_logo_for_{clean_name}_{clean_nisha}_gaming_style"
                banner_prompt = f"youtube_banner_art_for_{clean_name}_{clean_nisha}_hd_wallpaper"
                
                # Eng sodda va ishlaydigan URL struktura
                logo_url = f"https://image.pollinations.ai/prompt/{logo_prompt}?seed={seed_val}"
                banner_url = f"https://image.pollinations.ai/prompt/{banner_prompt}?seed={seed_val+1}"
                
                st.success("Rasmlar tayyor bo'ldi!")
                
                col_logo, col_banner = st.columns([1, 2])
                
                with col_logo:
                    st.subheader("🎯 Kanal Logotipi")
                    st.image(logo_url, caption=f"{kanal_nomi} Logo", use_container_width=True)
                
                with col_banner:
                    st.subheader("🖼️ Kanal Banneri")
                    st.image(banner_url, caption=f"{kanal_nomi} Banner", use_container_width=True)
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
        with st.spinner(f"{selected_model} strategiya tuzmoqda..."):
            prompt = f"""
            Hozirgi obunachilar: {sub_count}
            Maqsad: {goal}
            
            Ushbu YouTube kanali tezroq o'sishi uchun 30 kunlik aniq harakatlar rejasini va haftalik kontent rejasini o'zbek tilida tuzib ber.
            """
            javob = ask_ai(prompt)
            st.success("AI Tahlil yakunlandi!")
            st.markdown(javob)
