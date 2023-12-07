import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import altair as alt


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

        type_chart = st.selectbox(
            "Select chart type",
            ["Simple bar charts", "Line plot", "Pie", "Scatter", "Boxplot"],
        )
        st.header(type_chart)

        if type_chart == "Simple bar charts":
            st.bar_chart(head, x=x, y=y)
        elif type_chart == "Pie":
            fig = px.pie(head, names=x, values=y)
            st.plotly_chart(fig)
        elif type_chart == "Line plot":
            st.line_chart(head, x=x, y=y)
        elif type_chart == "Scatter":
            st.scatter_chart(head, x=x, y=y)
        elif type_chart == "Boxplot":
            chart = (
                alt.Chart(head)
                .mark_boxplot(extent="min-max")
                .encode(
                    x=alt.X(x, title=x),
                    y=alt.Y(y, title=y),
                )
            )
            # st.altair_chart(chart, theme="streamlit", use_container_width=True)

    with col1:
        st.header("Dataframe")
        st.dataframe(head)

# stuff to add:
# 10 figure  dans le cours data visualisation seaborn
