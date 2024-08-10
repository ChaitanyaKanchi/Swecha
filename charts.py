import streamlit as st
import pandas as pd
import numpy as np

df_01 = pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
)
st.table(df_01)

df_01 = pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
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

reset = st.button("Reset" ,type="primary")
if reset:
    st.write("Resetted")
st.write("Login botton")
learn = st.button("Login")
if learn:
    st.write("Succcessfully Login :smile:")
else:
    st.write("Click To login")



st.header("SKILLS")
st.subheader("MySQl")
rateing = st.slider("Rate your self on **MySQL**",0,5,2)
st.write("My rating in MySQL is ",rateing)

st.subheader("SQl")
rateing = st.slider("Rate your self on **SQL**",0,5,3)
st.write("My rating in SQL is ",rateing)

st.subheader("Python")
rateing = st.slider("Rate your self on **Python**",0,5,2)
st.write("My rating in Python is ",rateing)

st.subheader("HTML/CSS")
rateing = st.slider("Rate your self on **HTML/CSS**",0,5,2)
st.write("My rating in HTML/CSS is ",rateing)



st.header("Bar Chart")

df_02 = pd.DataFrame(
    {
        "col1" : np.random.rand(20),
        "col2" : np.random.randn(20),
        "col3" : np.random.choice(["A","B","C"],20)
    }
)
st.bar_chart(df_02,x="col1",y="col2",color="col3")




df = pd.DataFrame(
    np.random.randn(20,3),
    columns=["col1","col2","col3"]
)
st.bar_chart(df)
