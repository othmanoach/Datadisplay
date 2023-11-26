import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Import your .CSV file here:")
st.markdown("---")
file = st.file_uploader("Choose a .csv file", type=["csv"])

if file is not None:
    col1, col2 = st.columns(2)
    try:
        df = pd.read_csv(file, sep="[;,\t|:@]", engine='python')
    except Exception as e:
        st.error(f"Error: {e}")

    with col2:
        val_head = 5
        num_line = st.slider("Number of lines", min_value=1, max_value=len(df), value=val_head)
        head = df.head(num_line)

        x = st.selectbox("Select X value", df.columns)
        y = st.selectbox("Select Y value", df.columns)

        type_chart = st.selectbox("Select chart type", ['Simple bar charts', 'Simple area charts', 'Pie'])
        st.header(type_chart)

        if type_chart == 'Simple bar charts':
            st.bar_chart(head, x=x, y=y)
        elif type_chart == 'Simple area charts':
            st.area_chart(head, x=x, y=y)
        elif type_chart == 'Pie':
            fig = px.pie(head, names=x, values=y)
            st.plotly_chart(fig)

    with col1:
        st.header("Dataframe")
        st.dataframe(head.head(), hide_index=True)