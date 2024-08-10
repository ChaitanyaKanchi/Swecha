import streamlit as st
import pandas as pd
import numpy as np 


st.title("Media")

st.header("Audio")
st.audio("Manasukinta Alajadi.mp3" , format = "audio/mpeg", loop=True)

st.header("Image")

st.image("image.jpg",caption="music lover",width=600)

st.header("Icons")

st.header("Logo")

Horizantal_red = "youtube-logo.svg"
icon_red = "voice-search-icon.svg"
Horizantal_blue = "youtube-apps.svg"
icon_blue = "upload.svg"
options = [Horizantal_red,icon_red,Horizantal_blue,icon_blue]
sidebar_logo = st.selectbox("sidebar logo",options,0)
st.logo(sidebar_logo,icon_image = sidebar_logo)

st.header("Video")

video = open("video.mp4","rb")
video_bytes = video.read()
st.video(video_bytes)


st.header("Columns")

col1,col2,col3 = st.columns(3)
with col1:
    st.header("Column-1")
    st.write("This id column 1")

with col2:
    st.header("Column-2")
    st.write("This id column 2")

with col3:
    st.header("Column-3")
    st.write("This id column 3")



st.header("Containers")

with st.container(border = True):
    st.write("this is inside the container")
    st.bar_chart({"data":[1,2,3,4,5,6]})

st.write("This is outside the container")

st.header("Containers-grid")

row1 = st.columns(3)
row2 = st.columns(3)
for col in row1 + row2:
    tile = col.container(height = 120)
    tile.title(":balloon:")



@st.dialog("cast your vote")
def vote(item):
    st.markdown("Hello")
    st.write(f"Why did you vote to {item}")
    reason = st.text_input("Because..")
    if st.button("Submit"):
        st.session_state.vote(f"{item} is {reason}")
        st.rerun

if "vote" not in st.session_state:
    st.write("Cast your vote")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
    
else:
    f"you voted for {st.session_state.vote["item"]} beacause {st.session_state.vote["reason"]}"

