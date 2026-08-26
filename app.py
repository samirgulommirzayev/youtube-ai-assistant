import streamlit as st
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Ulusama AI — Multi-Model Assistant",
    page_icon="⚡",
    layout="wide"
)

# 2. Premium Oq va Sariq (Gold & Dark UI) CSS Dizayni
custom_css = """
<style>
    .stApp {
        background: linear-gradient(135deg, #0d0d0d 0%, #1a1a1a 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    .login-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 215, 0, 0.2);
        padding: 3rem;
        border-radius: 24px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
        max-width: 460px;
        margin: 50px auto;
        text-align: center;
    }
    
    .gold-header {
        background: linear-gradient(90deg, #FFFFFF 0%, #FFD700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 800;
    }
    
    /* Tablar stili */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(255, 255, 255, 0.02);
        padding: 8px;
        border-radius: 12px;
        border: 1px solid rgba(255, 215, 0, 0.1);
    }
    .stTabs [data-baseweb="tab"] {
        color: #cccccc;
        border-radius: 8px;
        padding: 8px 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FFD700 !important;
        color: #000000 !important;
        font-weight: bold;
    }
    
    /* Tugma stili */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%);
        color: #000000;
        border: none;
        padding: 0.85rem 1.5rem;
        border-radius: 12px;
        font-weight: 700;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.5);
        color: #000000;
    }

    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        border-radius: 10px !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. Kirish holati va parol
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

CORRECT_PASSWORD = "ulusama2026"

# 4. Yordamchi funksiyalar
def get_youtube_transcript(video_url):
    try:
        if "watch?v=" in video_url:
            video_id = video_url.split("watch?v=")[1].split("&")[0]
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[1].split("?")[0]
        else:
            return None, "Noto'g'ri YouTube havolasi."
            
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['uz', 'ru', 'en'])
        return " ".join([item['text'] for item in transcript_list]), None
    except Exception as e:
        return None, f"Subtitr yuklanmadi: {str(e)}"

# 5. Auth (Login/Parol)
if not st.session_state.authenticated:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<h1 class="gold-header">ULUSAMA AI</h1>', unsafe_allow_html=True)
    st.write("Platformaga kirish")
    st.write("---")
    
    with st.form("login_form"):
        username = st.text_input("Login:", placeholder="Loginni kiriting...")
        password = st.text_input("Parol:", type="password", placeholder="Parolni kiriting...")
        submit = st.form_submit_button("Kirish ⚡")
        
        if submit:
            if not username.strip() or not password.strip():
                st.error("⚠️ Login va parol maydonini to'ldirish majburiy!")
            elif password == CORRECT_PASSWORD:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("❌ Noto'g'ri parol!")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. Asosiy Multi-Tab Interfeys
else:
    col_t, col_l = st.columns([4, 1])
    with col_t:
        st.markdown('<h1 class="gold-header">⚡ Ulusama AI — Platform</h1>', unsafe_allow_html=True)
        st.write(f"Foydalanuvchi: **{st.session_state.username}**")
    with col_l:
        if st.button("Chiqish 🚪"):
            st.session_state.authenticated = False
            st.rerun()

    st.markdown("---")
    
    # 5 Ta Asosiy Tab
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📺 YouTube AI Agent", 
        "🤖 ChatGPT & Claude", 
        "⚡ Gemini Models", 
        "🔍 Perplexity Search", 
        "⚙️ API & Sozlamalar"
    ])
    
    # TAB 1: YouTube AI Assistant
    with tab1:
        st.subheader("YouTube Videolarni AI bilan Tahlil Qilish")
        yt_url = st.text_input("YouTube video havolasi:", placeholder="https://www.youtube.com/watch?v=...")
        prompt_yt = st.text_area("Topshiriq:", placeholder="Videoni qisqacha mazmuni va asosiy nuqtalarini chiqarib ber...")
        
        if st.button("Videoni Tahlil Qilish ✨"):
            if yt_url and prompt_yt:
                with st.spinner("Video tahlil qilinmoqda..."):
                    transcript, err = get_youtube_transcript(yt_url)
                    if err:
                        st.error(err)
                    else:
                        st.success("✅ Tahlil tayyor!")
                        st.write("Transkript asosidagi AI tahlili shu yerda ko'rinadi.")
            else:
                st.warning("Barcha maydonlarni to'ldiring!")

    # TAB 2: ChatGPT & Claude (OpenRouter)
    with tab2:
        st.subheader("ChatGPT & Claude Modellari")
        selected_model = st.selectbox("Modelni tanlang:", ["gpt-4o", "gpt-3.5-turbo", "claude-3-5-sonnet", "claude-3-haiku"])
        user_msg = st.text_area("Savolingizni kiriting:", height=120)
        if st.button("Yuborish (OpenRouter) 🚀"):
            st.info(f"{selected_model} modeliga so'rov yuborildi...")

    # TAB 3: Gemini Flash & Pro
    with tab3:
        st.subheader("Google Gemini Modellari")
        gemini_model = st.selectbox("Gemini Model:", ["gemini-1.5-flash", "gemini-1.5-pro"])
        gemini_prompt = st.text_area("Gemini uchun topshiriq:")
        if st.button("Gemini bilan ishlash ⚡"):
            st.info(f"{gemini_model} orqali ishlov berilmoqda...")

    # TAB 4: Perplexity Web Search
    with tab4:
        st.subheader("Perplexity — Qidiruv va Analitika")
        search_query = st.text_input("Internetdan nimani qidirmoqchisiz?")
        if st.button("Qidirish 🔍"):
            st.info("Qidiruv natijalari tayyorlanmoqda...")

    # TAB 5: API Sozlamalari & Status
    with tab5:
        st.subheader("Ulangan API Kalitlar Holati")
        st.write("• **GEMINI_API_KEY:** ", "✅ Ulangan" if os.getenv("GEMINI_API_KEY") else "❌ Topilmadi")
        st.write("• **OPENAI_API_KEY:** ", "✅ Ulangan" if os.getenv("OPENAI_API_KEY") else "❌ Topilmadi")
        st.write("• **OPENROUTER_API_KEY:** ", "✅ Ulangan" if os.getenv("OPENROUTER_API_KEY") else "❌ Topilmadi")
        st.write("• **BOT_TOKEN:** ", "✅ Ulangan (Telegram Bot faol)" if os.getenv("BOT_TOKEN") else "❌ Topilmadi")
