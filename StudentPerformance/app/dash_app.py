import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'notebooks')))

import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from utils import load_student_data

# Load data
df = load_student_data()

# Initialize Dash app
app = Dash(__name__)
app.title = "Student Performance Dashboard"

# Layout
app.layout = html.Div([
    html.H1("📊 Student Performance Dashboard (Dash)", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Select Gender:"),
        dcc.Dropdown(
            options=[{"label": g, "value": g} for g in df["gender"].unique()],
            value=df["gender"].unique()[0],
            id="gender-dropdown",
            clearable=False
        )
    ], style={"width": "300px", "margin": "20px auto"}),

    dcc.Graph(id="scatter-plot"),

    dcc.Graph(
        figure=px.box(
            df, x="test preparation course", y="average_score", color="performance_level",
            title="Box Plot: Average Score vs Test Preparation"
        )
    )
])

# Callback for interactivity
@app.callback(
    Output("scatter-plot", "figure"),
    Input("gender-dropdown", "value")
)
def update_scatter(selected_gender):
    filtered_df = df[df["gender"] == selected_gender]
    fig = px.scatter(
        filtered_df, x="math score", y="reading score", color="performance_level",
        title=f"Math vs Reading Scores ({selected_gender})",
        hover_data=["writing score"]
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)