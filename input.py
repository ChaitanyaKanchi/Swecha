import streamlit as st


st.header("Select Box")

option = st.selectbox(
    "What is your favorite color?",
    ('blue','red','green')
)
st.write("Your favorite color is ",option)


import streamlit as st

sentiment_mapping = ["one","two","three","four","five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")


sentiment_mapping = ["one","two","three","four","five"]
selected = st.feedback("faces")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s)")

sentiment_mapping = ["dislike", "like"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"you selected {sentiment_mapping[selected]}")

st.header("Link Botton")
st.link_button("Go To Youtube","https://www.youtube.com/")


color = st.color_picker("Pick A Color", "#00F208")
st.write("The current color is", color)


options = st.multiselect(
    "What is your favorite color?",
    ["Red","Green","Blue","Yellow","orange"],
    ["Red","orange"],
)
st.write("your favorite color is ",options)

options = st.radio(
    "What is your favarite movie",
    ["Kalki","OG","Devara"],
    index=None,
)
st.write("Your favarite movie is ",options)

import streamlit as st

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()


