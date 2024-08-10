import streamlit as st
import pandas as pd
import numpy as np

st.write("This is a Practice File")
st.title("Intenship")
st.header("Hi Chaitanya!!!")
st.subheader("Welcome to Swecha")
st.write('''We are excited to welcome chaitanya as our new intern. Currently studying Btech at KHIT, 
          has shown remarkable academic achievements and a strong interest in Web Development. 
         Actively participating in Hackthons, Chaitanya has honed skills 
         in HTML,CSS,JavaScript,MySQl,SQL,Python. Their passion for Web Development and proactive learning approach
          make them a valuable addition to our team. chaitanya will be working with swecha on 
         projects, bringing fresh perspectives and enthusiasm. Join us in welcoming chaitanya; 
         we look forward to a productive internship together.''')

st.header("Skills")
st.subheader("HTML/CSS")
range = st.slider(
    "Enter your scale on rating in HTML/CSS",
    0,5,2
)
st.write(f"Your rating on HTML/CSS is ",range)
st.subheader("Python")
range_01 = st.slider(
    "Enter your scale on rating in Python",
    0,5,2
)
st.write(f"Your rating on Python is ",range_01)
st.subheader("MySQL")
range_02 = st.slider(
    "Enter your scale on rating in MySQl",
    0,5,2
)
st.write(f"Your rating on MySQL is ",range_02)
st.subheader("SQL")
range_03 = st.slider(
    "Enter your scale on rating in SQL ",
    0,5,2
)
st.write(f"Your rating on SQL is ",range_03)

reset = st.button("Reset", type="primary")
login = st.button("Login")
if login:
    st.write("Succesfully Login")
else:
    st.write("Click to Login")


st.link_button("Click to YouTube","https://www.youtube.com/watch?v=Yk-unX4KnV4")


df = ["one","two","three","four","five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"your rating was {df[selected]}")

st.checkbox("I Accept")

st.color_picker(
    "Select color","#00F208"
)

st.multiselect(
    "Select your favorite color",
    ["red","blue","green","pink","yellow"],
    ["red"]
)

st.radio(
    "select fav movie",
    ["OG","Devara","Kalki"],
    index=None,
)

st.selectbox(
    "Select most used platform",
    ["Google","youtube","Facebook"]
)

st.toggle("Accept")

st.number_input(
    "Enter your weight"
)

st.date_input("Enter your date of birth")

st.time_input("Enter your birth time")

text = st.text_area("Introduce about your self")
z = len(text)
st.write("Total letters are ",z)


st.chat_input("Enter message")

st.text_input("Enter text")



df_01 = pd.DataFrame(
    np.random.randn(20,3),
    columns=(["A","B","c"])
)
st.table(df_01)


df_01 = pd.DataFrame(
    np.random.randn(20,3),
    columns=(["A","B","c"])
)
st.line_chart(df_01)


df_01 = pd.DataFrame(
    {
        "col1" : np.random.randn(20),
        "col2" : np.random.randn(20),
        "col3" : np.random.choice(["A","B","C"],20)
    }
)
st.line_chart(df_01,x="col1",y="col2",color="col3")

df_01 = pd.DataFrame(
    {
        "col1" : np.random.randn(20),
        "col2" : np.random.randn(20),
        "col3" : np.random.choice(["A","B","C"],20)
    }
)
st.bar_chart(df_01,x="col2",y="col1",color="col3")

df_01 = pd.DataFrame(
    {
        "col1" : np.random.randn(20),
        "col2" : np.random.randn(20),
        "col3" : np.random.choice(["A","B","C"],20)
    }
)
st.area_chart(df_01,x="col1",y="col2",color="col3")

df_01 = pd.DataFrame(
    {
        "col1" : np.random.randn(20),
        "col2" : np.random.randn(20),
        "col3" : np.random.choice(["A","B","C"],20)
    }
)
st.scatter_chart(df_01,x="col1",y="col2",color="col3")



