import streamlit as st

st.set_page_config(
    page_title="AI Career Advisor India",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        text-align: center;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        border: none;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'hobbies' not in st.session_state:
    st.session_state.hobbies = []
if 'result' not in st.session_state:
    st.session_state.result = None

st.markdown('<h1 class="main-title">🎯 AI Career Advisor India</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover Your Perfect Career Path After 10th Std</p>', unsafe_allow_html=True)

st.info("👈 Use the sidebar to navigate. Start with **Home** → **Assessment** → **Hobbies** → **Result**")