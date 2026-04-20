import streamlit as st
import json

st.title("🛣️ Your Career Roadmap")

if 'selected_career' in st.session_state:
    career = st.session_state.selected_career
    st.subheader(f"{career['icon']} {career['name']}")
else:
    st.info("Please select a career from Results or Explore page first")
    st.stop()

# Timeline
st.markdown("## 📅 Step-by-Step Timeline")

timeline = f"""
### 🟢 **After 10th (Age 15-16)**
**Stream Selection:**
{career['after_10th']}

**What to do NOW:**
- Focus on {', '.join(career['skills'][:2])}
- Start watching: {', '.join(career['youtube'][:2])}
- Join related hobby clubs

---

### 🔵 **Class 11th-12th (Age 16-18)**
**Exam Preparation:**
- Target exams: **{', '.join(career['exams'])}**
- Join coaching or online platforms
- Build foundational skills

**Resources:**
📺 YouTube: {', '.join(career['youtube'])}

---

### 🟡 **After 12th (Age 18-19)**
**Entrance Exams & Admissions:**
- Appear for: {', '.join(career['exams'])}
- Apply to: {', '.join(career['colleges'][:3])}

**Alternate Path:**
{career.get('alternate_path', 'No alternate path specified')}

---

### 🟠 **College/Training (Age 19-23)**
**Degree/Certification:**
- Complete your course
- Internships & projects
- Build portfolio/resume
- Network with professionals

---

### 🔴 **Start Career (Age 23+)**
**First Job/Practice:**
- Entry-level positions
- Continuous learning
- Certifications
- Build experience
"""

st.markdown(timeline)

# Pros and Cons
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✅ Why This Career?")
    for pro in career['pros']:
        st.success(f"✓ {pro}")

with col2:
    st.markdown("### ⚠️ Challenges to Know")
    for con in career['cons']:
        st.warning(f"⚠ {con}")

# Resources
st.divider()
st.markdown("## 📚 Learning Resources")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**📺 YouTube Channels:**")
    for yt in career['youtube']:
        st.info(f"• {yt}")

with col2:
    st.markdown("**🏫 Top Colleges:**")
    for college in career['colleges']:
        st.info(f"• {college}")

# Download
st.divider()
if st.button("📄 Download Complete Roadmap PDF", use_container_width=True):
    st.balloons()
    st.success("PDF generation feature coming soon! For now, take a screenshot 📸")