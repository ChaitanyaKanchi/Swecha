import streamlit as st
import pandas as pd
import numpy as np
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu

navbar = st_navbar(["Home","Education","Skills","Contact"])
st.write(navbar)

with st.sidebar:
    selected = option_menu("Menu",["Home","Settings"],icons = ["house","gear"],default_index = 1)



st.header("Checkbox")
st.write(
    "Select your favorite food", 
)

ice_cream = st.checkbox("Ice Cream")
biryani = st.checkbox("Biryani")
pizza = st.checkbox("Pizza")


st.subheader("Result")
if ice_cream:
    st.write("Your favorite food is ice cream")
if biryani:
    st.write("Your favorite food is biryani")
if pizza:
    st.write("Your favorite food is pizza")


st.latex("2x^2+3x^2+4x^3 = x^{n-1}+\sum_{k=0}^{n-1}")


st.header("File Uploader")

file_uploaded = st.file_uploader("Choose csv file")
if file_uploaded is not None:
    d1 = pd.read_csv(file_uploaded)
    st.write(d1)
    st.write(d1.describe())





    