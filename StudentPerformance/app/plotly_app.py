# TO RUN - python plotly_app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'notebooks')))

import pandas as pd
import plotly.express as px
from utils import load_student_data

# Load feature-engineered data
df = load_student_data()

# 1. Histogram of average scores
fig1 = px.histogram(df, x="average_score", color="performance_level",
                    nbins=30, title="Distribution of Average Scores",
                    labels={"average_score": "Average Score"})

# 2. Scatter plot: Math vs Reading
fig2 = px.scatter(df, x="math score", y="reading score", color="performance_level",
                  title="Math vs Reading Score by Performance")

# 3. Box plot of scores by test prep
fig3 = px.box(df, x="test preparation course", y="average_score", color="performance_level",
              title="Average Scores by Test Prep Status")

# Show plots
fig1.show()
fig2.show()
fig3.show()