import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.scorer import calculate_scores, get_top_clusters
from utils.recommender import recommend_careers
import plotly.graph_objects as go

st.title("🎯 Your Career Matches!")

if not st.session_state.answers or not st.session_state.hobbies:
    st.error("Please complete assessment and hobbies first!")
    st.stop()

# Calculate
scores = calculate_scores(st.session_state.answers, st.session_state.hobbies)
top_clusters = get_top_clusters(scores, 3)
recommendations = recommend_careers(top_clusters)

st.session_state.result = recommendations

# Show top 3
st.balloons()
st.success("🎉 Based on your answers, here are your TOP 3 career clusters:")

for i, rec in enumerate(recommendations):
    with st.container(border=True):
        st.markdown(f"## #{i+1} - {rec['info']['name']}")
        st.caption(rec['info']['desc'])
        st.markdown("**Suggested Careers:**")
        cols = st.columns(5)
        for j, career in enumerate(rec['careers']):
            with cols[j]:
                st.info(career)

# Radar chart
st.divider()
st.subheader("📊 Your Personality Profile")

categories = list(scores.keys())
values = list(scores.values())

fig = go.Figure(data=go.Scatterpolar(
    r=values,
    theta=categories,
    fill='toself',
    line_color='#764ba2'
))
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True)),
    showlegend=False,
    height=400
)
st.plotly_chart(fig, use_container_width=True)

# Next steps
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🛣️ See My Roadmap", use_container_width=True):
        st.switch_page("pages/06_roadmap.py")
with col2:
    if st.button("🔍 Explore More Careers", use_container_width=True):
        st.switch_page("pages/05_explore_career.py")
with col3:
    if st.button("📄 Download PDF Report", use_container_width=True):
        st.info("PDF generation coming up!")