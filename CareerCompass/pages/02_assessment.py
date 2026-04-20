import streamlit as st
import json

st.title("📝 Career Assessment")
st.caption("Answer honestly — there are no wrong answers!")

questions = [
    # Category 1: Analytical Thinking
    {"q": "When solving a problem, you prefer to:", 
     "options": ["Break it into logical steps", "Find creative solutions", "Discuss with others", "Try different approaches"],
     "category": "analytical"},
    {"q": "Math and numbers feel:", 
     "options": ["Fun and easy", "Okay if needed", "Boring", "Difficult"],
     "category": "analytical"},
    {"q": "Do you enjoy puzzles/Sudoku?", 
     "options": ["Love them!", "Sometimes", "Rarely", "Never"],
     "category": "analytical"},
    {"q": "Science experiments excite you because:", 
     "options": ["I love discovering how things work", "They're visually cool", "Group activity is fun", "Not really interested"],
     "category": "analytical"},
    
    # Category 2: Creativity
    {"q": "In free time, you'd rather:", 
     "options": ["Draw/Design something", "Read books", "Play sports", "Watch tutorials"],
     "category": "creative"},
    {"q": "When you see a beautiful building, you think:", 
     "options": ["Who designed this?", "How was it built?", "Nice photo spot!", "Nothing special"],
     "category": "creative"},
    {"q": "Do you enjoy writing stories/poems?", 
     "options": ["Yes, regularly", "Occasionally", "Only for school", "No"],
     "category": "creative"},
    {"q": "Music/Art classes are:", 
     "options": ["My favorite!", "Fun", "Just okay", "Boring"],
     "category": "creative"},
    
    # Category 3: Social/People Skills
    {"q": "In group projects, you usually:", 
     "options": ["Lead the team", "Contribute ideas", "Do assigned work", "Prefer working alone"],
     "category": "social"},
    {"q": "Helping others makes you feel:", 
     "options": ["Extremely happy", "Good", "Neutral", "It's their problem"],
     "category": "social"},
    {"q": "Public speaking is:", 
     "options": ["Exciting!", "Manageable", "Scary but doable", "Terrifying"],
     "category": "social"},
    {"q": "You enjoy teaching friends:", 
     "options": ["Yes, often", "Sometimes", "If asked", "Not really"],
     "category": "social"},
    
    # Category 4: Practical/Hands-on
    {"q": "Fixing broken things at home:", 
     "options": ["I love trying!", "I help dad/mom", "I watch", "I call repairman"],
     "category": "practical"},
    {"q": "Cooking/Gardening interests you:", 
     "options": ["A lot", "Sometimes", "Rarely", "Never"],
     "category": "practical"},
    {"q": "Working outdoors vs indoors:", 
     "options": ["Outdoors any day!", "Mix of both", "Mostly indoors", "Always indoors"],
     "category": "practical"},
    {"q": "Sports/Physical activities:", 
     "options": ["Daily passion", "Few times a week", "Occasionally", "Rarely"],
     "category": "practical"},
    
    # Category 5: Business/Leadership
    {"q": "If given ₹1000, you would:", 
     "options": ["Invest/Start small business", "Save it", "Buy something useful", "Spend on fun"],
     "category": "business"},
    {"q": "Negotiating prices in market:", 
     "options": ["I'm great at it!", "Decent", "Awkward", "I avoid it"],
     "category": "business"},
    {"q": "Planning events/trips:", 
     "options": ["I take charge", "I help plan", "I follow plans", "I just show up"],
     "category": "business"},
    {"q": "Watching Shark Tank / business shows:", 
     "options": ["I love them!", "Interesting", "Sometimes", "Boring"],
     "category": "business"}
]

# Progress
total = len(questions)
answered = len(st.session_state.answers)
st.progress(answered / total)
st.caption(f"Progress: {answered}/{total}")

# Display questions
for i, q in enumerate(questions):
    st.markdown(f"### Q{i+1}. {q['q']}")
    answer = st.radio(
        "Select one:",
        q['options'],
        key=f"q_{i}",
        index=None,
        label_visibility="collapsed"
    )
    if answer:
        st.session_state.answers[f"q_{i}"] = {
            "answer": answer,
            "score": 4 - q['options'].index(answer),  # 4,3,2,1
            "category": q['category']
        }
    st.divider()

# Navigation
col1, col2 = st.columns(2)
with col2:
    if len(st.session_state.answers) == total:
        if st.button("➡️ Next: Choose Hobbies", use_container_width=True):
            st.switch_page("pages/03_hobbies.py")
    else:
        st.warning(f"Please answer all {total} questions ({total - answered} remaining)")