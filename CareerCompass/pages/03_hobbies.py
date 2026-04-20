import streamlit as st

st.title("🎨 What Do You Love Doing?")
st.caption("Select ALL hobbies that interest you (minimum 3)")

hobbies = {
    "🎨 Drawing/Painting": "creative",
    "📚 Reading Books": "analytical",
    "🎮 Gaming": "tech",
    "💻 Coding": "tech",
    "🏏 Cricket/Sports": "physical",
    "🎵 Music/Singing": "creative",
    "💃 Dancing": "creative",
    "📷 Photography": "creative",
    "🍳 Cooking": "practical",
    "🌱 Gardening": "practical",
    "✍️ Writing": "creative",
    "🧪 Science Experiments": "analytical",
    "🤖 Robotics": "tech",
    "🎭 Acting/Drama": "creative",
    "🗣️ Public Speaking": "social",
    "👥 Helping People": "social",
    "🏃 Fitness/Yoga": "physical",
    "🎬 Making Videos": "creative",
    "🧩 Puzzles": "analytical",
    "🛠️ Building/DIY": "practical",
    "💰 Stock Market": "business",
    "🌍 Traveling": "social",
    "🐕 Animal Care": "social",
    "♟️ Chess/Strategy Games": "analytical"
}

# Display in grid
cols = st.columns(4)
selected = []

for i, (hobby, cat) in enumerate(hobbies.items()):
    with cols[i % 4]:
        if st.checkbox(hobby, key=f"hobby_{i}"):
            selected.append({"name": hobby, "category": cat})

st.session_state.hobbies = selected

st.divider()
st.info(f"✅ Selected: **{len(selected)}** hobbies")

col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Back to Questions"):
        st.switch_page("pages/02_assessment.py")
with col2:
    if len(selected) >= 3:
        if st.button("🎯 Get My Career Matches!", use_container_width=True):
            st.switch_page("pages/04_result.py")
    else:
        st.warning("Please select at least 3 hobbies")