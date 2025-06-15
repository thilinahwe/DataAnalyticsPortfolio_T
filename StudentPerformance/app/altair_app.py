# TO RUN - python altair_app.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'notebooks')))

import pandas as pd
import altair as alt
from utils import load_student_data

# Load data
df = load_student_data()

# Chart 1: Bar chart - Average Score by Gender & Performance Level
bar_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('gender:N', title='Gender'),
    y=alt.Y('average_score:Q', title='Average Score', aggregate='mean'),
    color='performance_level:N',
    column='performance_level:N'
).properties(
    title='Average Score by Gender and Performance Level'
)

# Chart 2: Scatter plot with tooltip
scatter_chart = alt.Chart(df).mark_circle(size=70).encode(
    x='math score',
    y='reading score',
    color='performance_level',
    tooltip=['gender', 'math score', 'reading score', 'writing score', 'performance_level']
).properties(
    title='Math vs Reading Scores with Tooltips'
).interactive()

# Display charts
bar_chart.show()
scatter_chart.show()