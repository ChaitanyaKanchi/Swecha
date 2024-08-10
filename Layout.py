import streamlit as st
import pandas as pd
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu

page = st_navbar(["Home","About","Education","Skills","Contact"])
st.write(page)

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected



st.sidebar.header("Input")
user_name = st.sidebar.text_input("Enter your name")
emoji =st.sidebar.selectbox("choose your fav emoji ",['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
food = st.sidebar.selectbox("choose your fav food", ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header("How to layout your streamlit app")

with st.expander("About this app"):
    st.write("This app shows the various ways on how you can layout your Streamlit app.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",width=250)

st.header("Output")

col1,col2,col3 = st.columns(3)

with col1:
    if user_name != '':
        st.write("Your name is ",user_name)
    else:
        st.write("Please enter your name")

with col2:
    if emoji != '':
        st.write(f"{emoji} is your fav emoji")
    else:
        st.write("please select fav emoji")

with col3:
    if food != '':
        st.write(f"{food} is your fav food")
    else:
        st.write("please enter your fav food")


