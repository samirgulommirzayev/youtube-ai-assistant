import streamlit as st

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Ulusama AI", page_icon="🚀", layout="wide")

# 2. Zamonaviy CSS va JavaScript (Animatsiyali quyuq rejim dizayni)
custom_css = """
<style>
    /* Asosiy fon va shriftlar */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* Kirish kartasi dizayni */
    .login-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        max-width: 450px;
        margin: 40px auto;
        text-align: center;
    }
    
    /* Sarlavha animatsiyasi */
    .login-title {
        background: linear-gradient(90deg, #6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 10px;
    }

    /* Tugma stili */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(99, 102, 241, 0.4);
    }
</style>

<script>
    // Tugma bosilganda yengil effekt beruvchi JS
    document.addEventListener('DOMContentLoaded', () => {
        const buttons = document.querySelectorAll('button');
        buttons.forEach(btn => {
            btn.addEventListener('click', () => {
                btn.style.transform = 'scale(0.98)';
                setTimeout(() => btn.style.transform = 'none', 100);
            });
        });
    });
</script>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. Seans holatini tekshirish
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Aniq belgilangan parol
CORRECT_PASSWORD = "ulusama2026"

# 4. Login interfeysi
if not st.session_state.authenticated:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<h1 class="login-title">Ulusama AI</h1>', unsafe_allow_html=True)
    st.write("Tizimga kirish uchun ma'lumotlarni kiriting:")
    
    with st.form("login_form"):
        username = st.text_input("Login (Ismingiz):", placeholder="Hohlagan ismingizni yozing...")
        password = st.text_input("Parol:", type="password", placeholder="Parolni kiriting...")
        submit_button = st.form_submit_button("Kirish 🚀")
        
        if submit_button:
            # Login va parol to'ldirilganligi hamda parol to'g'riligini tekshirish
            if not username.strip() or not password.strip():
                st.error("⚠️ Login va parol maydonlarini to'ldirish majburiy!")
            elif password == CORRECT_PASSWORD:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("❌ Parol noto'g mehmonga kiritildi!")
                
    st.markdown('</div>', unsafe_allow_html=True)

# 5. Asosiy dastur (Kirish muvaffaqiyatli bo'lganda)
else:
    st.title(f"🚀 Xush kelibsiz, {st.session_state.username}!")
    st.write("Ulusama AI platformasi muvaffaqiyatli ishga tushdi.")
    
    if st.button("Tizimdan chiqish"):
        st.session_state.authenticated = False
        st.rerun()
