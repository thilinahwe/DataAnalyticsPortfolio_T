# to RUN - streamlit run streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'notebooks')))

from utils import load_student_data
from sklearn.ensemble import RandomForestClassifier


# Load data & train a model quickly
df = load_student_data()
X = df[['math score', 'reading score', 'writing score']]
y = df['performance_label']

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Streamlit UI
st.title("🎓 Student Performance Classifier")
st.write("Input the student's test scores below:")

math = st.slider("Math Score", 0, 100, 70)
reading = st.slider("Reading Score", 0, 100, 70)
writing = st.slider("Writing Score", 0, 100, 70)

input_data = pd.DataFrame([[math, reading, writing]], columns=X.columns)

prediction = model.predict(input_data)[0]
label_map = {0: "Low", 1: "Medium", 2: "High"}
st.subheader(f"📈 Predicted Performance Level: {label_map[prediction]}")

