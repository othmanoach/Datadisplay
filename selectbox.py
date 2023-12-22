import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import altair as alt
import plotly.figure_factory as ff
from chart import *


# "Histogram",
#                 "Line plot",
#                 "Pie",
#                 "Boxplot",
#                 "KDE plot",
#                 "Bar plot",
#                 "Scatter plot",
#                 "Heatmap",
#                 "Violin plot"
def chose(type_chart, data, x, y):
    match type_chart:
        case "Histogram":
            histogram(data, x, y)
        # ------------------------------------------------------------------------
        case "Pie":
            pie(data, x, y)
        # ------------------------------------------------------------------------
        case "Line plot":
            line_plot(data, x, y)
        case "Scatter plot":
            scatter_chart(data, x, y)
        # ------------------------------------------------------------------------
        case "Boxplot":
            boxplot(data, x, y)
        case "Bar plot":
            bar_plot(data, x, y)
        case "KDE plot":
            kde_plot(data, x, y)
        case "Violin plot":
            violin_plot(data, x, y)
        case "Heatmap":
            heatmap(data, x, y)
