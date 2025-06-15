import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'notebooks')))

import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import column
from bokeh.palettes import Category10
from utils import load_student_data

# Load data
df = load_student_data()

# Output to HTML file
output_file("bokeh_student_dashboard.html")

# Map performance level to color
color_map = {"Low": Category10[3][0], "Medium": Category10[3][1], "High": Category10[3][2]}
df["color"] = df["performance_level"].map(color_map)

# Create ColumnDataSource
source = ColumnDataSource(df)

# Plot 1: Scatter plot (math vs reading)
scatter = figure(title="Math vs Reading Score", width=700, height=400,
                 x_axis_label="Math Score", y_axis_label="Reading Score", tools="pan,wheel_zoom,box_zoom,reset,hover,save")

scatter.circle("math score", "reading score", size=8, source=source, color="color", legend_field="performance_level")

scatter.add_tools(HoverTool(
    tooltips=[
        ("Gender", "@gender"),
        ("Math", "@{math score}"),
        ("Reading", "@{reading score}"),
        ("Writing", "@{writing score}"),
        ("Level", "@performance_level"),
    ]
))

scatter.legend.title = "Performance Level"

# Plot 2: Histogram of average scores
hist = figure(title="Average Score Distribution", width=700, height=300,
              x_axis_label="Average Score", y_axis_label="Count")

hist.quad(top=df["average_score"].value_counts().sort_index().values,
          bottom=0,
          left=df["average_score"].value_counts().sort_index().index - 0.5,
          right=df["average_score"].value_counts().sort_index().index + 0.5,
          fill_color="navy", line_color="white", alpha=0.7)

# Show both plots in one HTML
show(column(scatter, hist))