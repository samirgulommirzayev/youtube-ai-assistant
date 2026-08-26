import streamlit as st
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="Ulusama AI — YouTube Assistant",
    page_icon="⚡",
    layout="wide"
)

# 2. Premium Oq va Sariq (Gold & Clean White) CSS Dizayni
custom_css = """
<style>
    /* Asosiy fon va matn ranglari */
    .stApp {
        background: linear-gradient(135deg, #0d0d0d 0%, #1a1a1a 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Login kartasi */
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
    
    /* Sarlavha gradienti (Oq va Yashin Sariq) */
    .gold-header {
        background: linear-gradient(90deg, #FFFFFF 0%, #FFD700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.6rem;
        font-weight: 800;
        letter-spacing: -1px;
    }
    
    /* Sariq tugmalar stili */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%);
        color: #000000;
        border: none;
        padding: 0.85rem 1.5rem;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 215, 0, 0.5);
        color: #000000;
    }
    
    /* Input maydonlari */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        border-radius: 10px !important;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #FFD700 !important;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.4) !important;
    }
    
    /* Kartalar va konteynerlar */
    .result-card {
        background: rgba(255, 255, 255, 0.02);
        border-left: 4px solid #FFD700;
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 1.5rem;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. Seans holatini tekshirish
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

CORRECT_PASSWORD = "ulusama2026"

# 4. YouTube Subtitrni olish funksiyasi
def get_youtube_transcript(video_url):
    try:
        if "watch?v=" in video_url:
            video_id = video_url.split("watch?v=")[1].split("&")[0]
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[1].split("?")[0]
        else:
            return None, "Noto'g'ri YouTube havolasi."
            
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['uz', 'ru', 'en'])
        transcript_text = " ".join([item['text'] for item in transcript_list])
        return transcript_text, None
    except Exception as e:
        return None, f"Subtitrni yuklab bo'lmadi: {str(e)}"

# 5. Gemini AI orqali tahlil qilish funksiyasi
def analyze_with_gemini(prompt_text, transcript_text):
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "⚠️ API Kalit topilmadi! Render muhit o'zgaruvchilarini tekshiring."
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    full_prompt = f"""
    Siz professional YouTube yordamchisiz.
    Quyidagi video transkriptidan foydalanib foydalanuvchi savoliga javob bering:
    
    Transkript:
    {transcript_text[:10000]}
    
    Foydalanuvchi topshirig'i:
    {prompt_text}
    """
    response = model.generate_content(full_prompt)
    return response.text

# 6. Auth / Login Oynasi
if not st.session_state.authenticated:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<h1 class="gold-header">ULUSAMA AI</h1>', unsafe_allow_html=True)
    st.write("Tizimga kirish uchun ma'lumotlarni kiriting")
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

# 7. Asosiy YouTube Assistant interfeysi
else:
    col_title, col_logout = st.columns([4, 1])
    with col_title:
        st.markdown('<h1 class="gold-header">⚡ Ulusama AI — YouTube Assistant</h1>', unsafe_allow_html=True)
        st.write(f"Xush kelibsiz, **{st.session_state.username}**!")
    with col_logout:
        if st.button("Chiqish 🚪"):
            st.session_state.authenticated = False
            st.rerun()

    st.markdown("---")
    
    col_in1, col_in2 = st.columns([1, 1])
    
    with col_in1:
        yt_link = st.text_input("🔗 YouTube Video Havolasi:", placeholder="https://www.youtube.com/watch?v=...")
        prompt = st.text_area("💬 Topshiriq yoki Savol:", placeholder="Masalan: Videoni qisqacha mazmunini va asosiy 3 ta g'oyasini aytib ber...", height=150)
        start_btn = st.button("Tahlilni Boshlash ✨")

    with col_in2:
        if start_btn:
            if not yt_link.strip() or not prompt.strip():
                st.warning("⚠️ Iltimos, video havolasi va topshiriqni to'liq kiriting!")
            else:
                with st.spinner("⚡ Video tahlil qilinmoqda..."):
                    transcript, error = get_youtube_transcript(yt_link)
                    if error:
                        st.error(f"❌ Xatolik: {error}")
                    else:
                        ai_response = analyze_with_gemini(prompt, transcript)
                        st.markdown('<div class="result-card">', unsafe_allow_html=True)
                        st.subheader("📝 AI Natijasi:")
                        st.write(ai_response)
                        st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("👈 Chap tomonda video havolasini kiriting va topshiriq berib 'Tahlilni Boshlash' tugmasini bosing.")
