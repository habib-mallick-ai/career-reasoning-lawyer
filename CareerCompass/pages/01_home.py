import streamlit as st

st.title("🏡 Welcome, Future Achiever!")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🌟 Your Future Starts Here
    
    Confused about what to do after 10th? You're not alone! 
    
    **This tool will help you:**
    - 🧠 Discover your strengths
    - 💖 Match careers with your hobbies
    - 🛣️ Get a clear roadmap (Stream → Exam → College)
    - 📚 Find free learning resources
    - 📄 Download your personalized report
    
    ### 🎯 How It Works
    1. **Take 20 quick questions** (5 minutes)
    2. **Select your hobbies**
    3. **Get TOP 3 career matches**
    4. **Explore 100+ career options**
    5. **Download your roadmap PDF**
    """)
    
    if st.button("🚀 Start Assessment", use_container_width=True):
        st.switch_page("pages/02_assessment.py")

with col2:
    st.markdown("### 💡 Did You Know?")
    st.success("There are **250+ career options** in India today, not just Doctor or Engineer!")
    st.warning("Choose career based on **PASSION**, not just salary 💖")
    st.info("Top performers love what they do. Find YOUR thing! 🌟")