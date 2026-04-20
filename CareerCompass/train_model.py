import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# -----------------------------
# CAREER CLUSTERS
# -----------------------------
# 0 = Analytical
# 1 = Creative
# 2 = Social
# 3 = Entrepreneurial
# 4 = Technical
# 5 = Research

data = []

for i in range(800):
    logic = np.random.randint(1, 6)
    creativity = np.random.randint(1, 6)
    communication = np.random.randint(1, 6)
    risk = np.random.randint(1, 6)
    tech_interest = np.random.randint(1, 6)
    curiosity = np.random.randint(1, 6)

    # -----------------------------
    # Labeling logic (AI simulation)
    # -----------------------------
    if logic + tech_interest > creativity + communication:
        label = 4  # Technical
    elif creativity > logic and creativity > communication:
        label = 1  # Creative
    elif communication > logic and communication > creativity:
        label = 2  # Social
    elif risk > 3 and communication > 3:
        label = 3  # Entrepreneurial
    elif curiosity > 4 and logic > 3:
        label = 5  # Research
    else:
        label = 0  # Analytical

    data.append([logic, creativity, communication, risk, tech_interest, curiosity, label])

df = pd.DataFrame(data, columns=[
    "Logic", "Creativity", "Communication", "Risk", "Tech", "Curiosity", "Label"
])

X = df.drop("Label", axis=1)
y = df["Label"]

# -----------------------------
# Train Model
# -----------------------------
model = DecisionTreeClassifier()
model.fit(X, y)

# -----------------------------
# Save Model
# -----------------------------
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")
