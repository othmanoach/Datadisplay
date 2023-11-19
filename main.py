import streamlit as st
import pandas as pd
import os
st.title("Import your .CSV file here :")
st.markdown("---")
file = st.file_uploader("**Choose a .csv file**", type={"csv"})

if file is not None:
    col1, col2 = st.columns(2)
    df = pd.read_csv(file, sep="[;,\t|:@]",  engine='python')
    with col2:
        val_head = 5
        num_line = st.slider(
            "Number of line", min_value=1, max_value=len(df), value=val_head
        )
        head = df.head(num_line)
        #------------------------------------------
        st.header("Line Chart")
        x = st.selectbox("Select X value", df.columns)
        y = st.selectbox("Select Y value", df.columns)
        st.line_chart(head, x=x, y=y)


    with col1:
        st.header("Dataframe")
        st.dataframe(head, hide_index=True)