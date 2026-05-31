"""
charts.py

This file is used for chart-related helper information.
Main charts are created inside app.py using Matplotlib and Seaborn.
"""

CHART_PURPOSES = {
    "Pie Chart": "Shows part-to-whole distribution of glass types.",
    "Histogram": "Shows distribution of numerical chemical features.",
    "Line Chart": "Shows feature trend by sample ID.",
    "Bar Chart": "Compares average chemical values by glass type.",
    "Scatter Plot": "Shows relationship between two numerical features.",
    "Box Plot": "Shows spread and outliers.",
    "Heatmap": "Shows correlation between numerical features.",
    "Area Chart": "Shows cumulative feature trend.",
    "Count Plot": "Shows frequency of glass types.",
    "Violin Plot": "Shows distribution density by glass type."
}