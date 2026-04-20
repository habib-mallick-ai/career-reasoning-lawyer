import streamlit as st
import json

st.title("🔍 Explore 100+ Careers")
st.caption("Browse careers freely, no quiz needed!")

# Load careers
with open('data/careers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    careers = data['careers']

# Filters
col1, col2 = st.columns([3, 1])
with col1:
    search = st.text_input("🔎 Search careers", placeholder="e.g., engineer, doctor, designer")
with col2:
    category_filter = st.selectbox("Category", ["All", "tech", "creative", "analytical", "social", "practical", "business", "physical"])

# Filter careers
filtered = careers
if search:
    filtered = [c for c in filtered if search.lower() in c['name'].lower() or search.lower() in c['description'].lower()]
if category_filter != "All":
    filtered = [c for c in filtered if c['category'] == category_filter]

st.caption(f"Showing {len(filtered)} careers")

# Display careers
for career in filtered:
    with st.expander(f"{career['icon']} {career['name']}"):
        st.markdown(f"**{career['description']}**")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**📚 After 10th:**")
            st.info(career['after_10th'])
            
            st.markdown("**🎯 Skills Needed:**")
            st.write(", ".join(career['skills']))
            
            st.markdown("**📝 Exams:**")
            st.write(", ".join(career['exams']))
        
        with col2:
            st.markdown("**✅ Pros:**")
            for pro in career['pros']:
                st.success(f"• {pro}")
            
            st.markdown("**⚠️ Cons:**")
            for con in career['cons']:
                st.warning(f"• {con}")
        
        st.markdown("**🏫 Top Colleges:**")
        st.write(", ".join(career['colleges']))
        
        st.markdown("**📺 Learn More (YouTube):**")
        st.write(", ".join(career['youtube']))
        
        if st.button(f"🛣️ See Roadmap for {career['name']}", key=f"roadmap_{career['id']}"):
            st.session_state.selected_career = career
            st.switch_page("pages/06_roadmap.py")