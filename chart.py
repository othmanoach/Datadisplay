import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import altair as alt
import plotly.figure_factory as ff

"""charts"""
warn = "⚠️"


def pie(data, x, y):
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    """create a pie chart"""
    if x_dtype in ["float64", "int64", "datetime64[ns]"]:
        st.error("X should always be a string (category)", icon=warn)
    elif y_dtype == "object":
        st.error("Y should always be a number (value)", icon=warn)
    elif x == y:
        st.error("Please choose a X value different than Y", icon=warn)
    elif x_dtype == "object" and y_dtype == "object":
        st.error("X and Y cannot be both of type string (category)", icon=warn)
    else:
        fig = px.pie(data, names=x, values=y)
        st.plotly_chart(fig)


def line_plot(data, x, y):
    """create a line plot"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x_dtype not in ["float64", "int64", "datetime64[ns]"]:
        st.error(
            "X should be a numeric or datetime variable for a line plot.",
            icon=warn,
        )
    elif y_dtype not in ["float64", "int64", "datetime64[ns]"]:
        st.error("Y should be a numeric variable for a line plot.", icon=warn)
    elif len(data) < 2:
        st.error(
            "Insufficient data points for a line plot. Please choose a different dataset or adjust the number of lines.",
            icon=warn,
        )
    else:
        st.line_chart(data, x=x, y=y)


def histogram(data, x, y=None):
    """create histogram chart"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x == y:
        st.error("X and Y should be different", icon=warn)
    elif x_dtype == "object":
        st.error("X should be a numeric variable for an histogram", icon=warn)
    elif y and y_dtype == "object":
        st.error("Y should be a numeric variable for an histogram", icon=warn)
    elif len(data) < 1:
        st.error(
            "Insufficient data points for an histogram. Please choose a different dataset or adjust the number of lines.",
            icon=warn,
        )
    else:
        if y:
            fig = px.histogram(data, x=x, y=y)
        else:
            fig = px.histogram(data, x=x)
        st.plotly_chart(fig, use_container_width=True)


def boxplot(data, x, y):
    """create boxplot chart"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x_dtype != "object" or y_dtype == "object":
        st.error(
            "X should be a categorical variable and Y should be a numeric variable for a boxplot",
            icon=warn,
        )
    else:
        fig = px.box(data, x=x, y=y, points="all")
        st.plotly_chart(fig)
    # else:
    #     st.error(
    #         "X should be a categorical variable and Y should be a numeric variable for a boxplot",
    #         icon=warn,
    #     )
