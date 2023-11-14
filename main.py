import streamlit as st
import pandas as pd

st.title("Import your .CSV file here :")
st.markdown("---")
file = st.file_uploader("**Choose a .csv file**", type={"csv"})

if file is not None:
    # col1, col2 = st.columns(2)
    df = pd.read_csv(file)
    # #print(data)
    # with col1:
    #     val_head = 5
    #     if st.button("Max"):
    #         val_head = len(df)
    # with col2:
    #     num_line = st.number_input("Insert number of line :", min_value= 1, max_value = len(df), value= val_head)
    val_head = 5
    num_line = st.slider("Number of line", min_value=1, max_value=len(df), value= val_head)
    head = df.head(num_line)
    st.dataframe(head, hide_index=True)

    # st.write(data)
