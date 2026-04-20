def calculate_scores(answers, hobbies):
    """Calculate scores per category from answers + hobbies"""
    scores = {
        "analytical": 0,
        "creative": 0,
        "social": 0,
        "practical": 0,
        "business": 0,
        "tech": 0,
        "physical": 0
    }
    
    # Score from MCQ answers
    for key, val in answers.items():
        cat = val['category']
        if cat in scores:
            scores[cat] += val['score']
    
    # Boost from hobbies (each hobby adds 3 points)
    for hobby in hobbies:
        cat = hobby['category']
        if cat in scores:
            scores[cat] += 3
    
    return scores

def get_top_clusters(scores, top_n=3):
    """Return top N career clusters"""
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:top_n]