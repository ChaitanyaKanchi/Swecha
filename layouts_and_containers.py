import streamlit as st
import pandas as pd
import numpy as np


st.title("Layouts and Containers")

st.header("Columns")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column-1")
    st.write("This is column 1")

with col2:
    st.header("column-2")
    st.write("This is column 2")

with col3:
    st.header("column-3")
    st.write("This is column 3")

st.header("Columns with Alignment")

col1, col2, col3 = st.columns(3, vertical_alignment="center")

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


st.header("Columns with Ratios")

col1, col2 = st.columns([3,1])

with col1:
    df = pd.DataFrame(
        np.random.randn(10,3),
        columns=["a","b","c"]
    )
    st.line_chart(df)

with col2:
    df_1 = pd.DataFrame(
        np.random.randn(10,3),
        columns=["a","b","c"]
    )
    st.table(df_1)

st.header("Containers")

with st.container(border=True):
    st.write("This is inside a container")
    st.bar_chart(np.random.randn(10,3))
st.write("This is outside of the container")


st.header("Grid Method -- Horizantal")

row1 = st.columns(4)
row2 = st.columns(4)

for col in row1 + row2:
    grid = col.container(height = 120)
    grid.header(":balloon:")

st.header("Grid Method -- Vertical")

row1 = st.columns(4)

for col in row1:
    grid = st.container(height = 120)
    grid.header(":balloon:")


st.title("Dialog-Boxes")

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"


# """ 
#with st.empty():
   # for seconds in range(60):
  #      st.write(f"{seconds} seconds passed")
 #       time.sleep(1)
 #   st.write("1 minute over")

 #


st.header("Expanders")

st.bar_chart({"data":[1,2,3,4,5,6]})
with st.expander("see explanation"):
    st.write("This is explanation")
    st.table({"data":[1,2,3,4,5,6]})


st.header("Forms")

with st.form("My Form"):
    st.write("This is inside the form")
    slider = st.slider("select your fav number",1,5,2)
    check_box = st.checkbox("Confirm")

    submitted = st.form_submit_button("Submit")
    if submitted:
        if check_box:
            st.write(f"fav number {slider}")
        else:
            st.write("Please confirm")


st.header("Pop Over")

with st.popover("Open pop over"):
    st.markdown("Hello World")
    name = st.text_input("Enter your name")

st.write(f"your name is {name}")


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.header("Tabs")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)