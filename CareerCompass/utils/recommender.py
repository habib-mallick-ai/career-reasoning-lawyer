import json

CLUSTER_TO_CAREERS = {
    "analytical": ["Data Scientist", "Research Scientist", "Mathematician", "CA", "Economist"],
    "creative": ["Graphic Designer", "Animator", "Architect", "Fashion Designer", "Content Creator"],
    "social": ["Teacher", "Psychologist", "Lawyer", "Social Worker", "HR Manager"],
    "practical": ["Chef", "Civil Engineer", "Farmer/Agritech", "Mechanic", "Pilot"],
    "business": ["Entrepreneur", "Marketing Manager", "Investment Banker", "MBA", "Startup Founder"],
    "tech": ["Software Engineer", "AI Engineer", "Cybersecurity", "Game Developer", "App Developer"],
    "physical": ["Athlete", "Fitness Trainer", "Defense Officer", "Sports Coach", "Physiotherapist"]
}

CLUSTER_INFO = {
    "analytical": {"name": "🧠 Analytical Thinker", "desc": "You love logic, data, and solving complex problems"},
    "creative": {"name": "🎨 Creative Soul", "desc": "You see the world in colors, designs, and stories"},
    "social": {"name": "👥 People Person", "desc": "You thrive on connection and helping others grow"},
    "practical": {"name": "🛠️ Hands-On Builder", "desc": "You learn by doing and creating real things"},
    "business": {"name": "💼 Business Leader", "desc": "You have the mindset of an entrepreneur"},
    "tech": {"name": "💻 Tech Wizard", "desc": "Technology is your playground"},
    "physical": {"name": "💪 Action Hero", "desc": "You're built for action and physical excellence"}
}

def recommend_careers(top_clusters):
    """Return career recommendations based on top clusters"""
    recommendations = []
    for cluster, score in top_clusters:
        recommendations.append({
            "cluster": cluster,
            "info": CLUSTER_INFO[cluster],
            "careers": CLUSTER_TO_CAREERS[cluster],
            "score": score
        })
    return recommendations