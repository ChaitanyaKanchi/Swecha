import streamlit as st

st.title("Media")

st.header("Music")
st.audio("Manasukinta Alajadi.mp3",format="audio/mpeg",loop = True)

st.header("Image")
st.image("image.jpg",caption = "Music Lover",width = 600)


st.header("Logo")

Horizantal_red = "youtube-logo.svg"
icon_red = "voice-search-icon.svg"
Horizantal_blue = "youtube-apps.svg"
icon_blue = "upload.svg"
options = [Horizantal_red,icon_red,Horizantal_blue,icon_blue]
sidebar_logo = st.selectbox("sidebar logo",options,0)
st.logo(sidebar_logo,icon_image = sidebar_logo)


st.header("Video")

video_file = open("video.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

