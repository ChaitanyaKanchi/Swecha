import streamlit as st
import numpy as np
import pandas as pd 

prompt = st.chat_input("Enter your chat")
if prompt:
    st.write(prompt)
with st.chat_message("user"):
    st.write(prompt)


import time
download_btn = st.button("Download")
if download_btn:
    with st.status("Downloading data ... ",expanded = True) as status:
        st.write("Searching data ...")
        time.sleep(2)
        st.write("Found URL")
        time.sleep(1)
        st.write("Downloading data ...")
        time.sleep(1)
        status.update(
            label="Download completed!",state="complete",expanded = False
        )
    st.button("Rerun")

st.success('This is a success message!', icon="✅")

st.info('This is a purely informational message', icon="ℹ️")

st.warning('This is a warning', icon="⚠️")

st.error('This is an error', icon="🚨")

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Rerun")