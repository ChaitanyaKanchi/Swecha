import streamlit as st
import pandas as pd

file_uploaded = st.file_uploader("Choose a csv file")

if file_uploaded is not None:
    df = pd.read_csv(file_uploaded)
    st.write(df)
    st.write(df.describe())

