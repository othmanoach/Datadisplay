import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt
from chart import *
from selectbox import *
from statistics import median, mean, mode

st.title("Import your .CSV file here:")
st.markdown("---")
file = st.file_uploader("Choose a .csv file", type=["csv"])

if file is not None:
    col1, col2 = st.columns(2)
    try:
        df = pd.read_csv(file, sep="[;,\t|:@]", engine="python")
    except Exception as e:
        st.error(f"Error: {e}")

    with col2:
        val_head = 5
        num_line = st.slider(
            "Number of lines", min_value=1, max_value=len(df), value=val_head
        )
        head = df.head(num_line)

        x = st.selectbox("Select X value", df.columns)
        y = st.selectbox("Select Y value", df.columns)
        x_dtype = df[x].dtype
        y_dtype = df[y].dtype
        # print(x_dtype, y_dtype)

        type_chart = st.selectbox(
            "Select chart type",
            [
                "Histogram",
                "Line plot",
                "Pie",
                "Boxplot",
                "KDE plot",
                "Bar plot",
                "Scatter plot",
                "Heatmap",
                "Violin plot",
            ],
        )
        st.header(type_chart)
        # print(len(head))
        if len(head) < 2:
            st.error(
                "Insufficient data points. Please choose a different dataset or adjust the number of lines.",
                icon="⚠️",
            )
        else:
            chose(type_chart, head, x, y)
        with col1:
            st.header("Dataframe")
            st.dataframe(head)
            if x_dtype != "object":
                st.write("Mean of ", x, ":", mean(df[x]))
                st.write("Median of ",x,":",median(df[x]))
                st.write("Mode of ",x,":",mode(df[x]))
            if y_dtype != "object":
                st.write("Mean of ", y, ":", mean(df[y]))
                st.write("Median of ",y,":",median(df[y]))
                st.write("Mode of ",y,":",mode(df[y]))

# stuff to add:
# 10 figure  dans le cours data visualisation seaborn

# """pie""" DONE
# """line plot""" DONE
# """Scatter plot""" DONE
# """Histogram""" DONE
# """Boxplot""" DONE
# """KDE plot""" DOne
# """Violin plot"""
# """Bar plot"""
# """Heatmap"""
