import streamlit as st
import pandas as pd
import numpy as np

st.write("HI HELLO")

age = st.slider("How old are you",0,130,25)
st.write("I am",age,"old")

range = st.slider("select a range of vales",0.0, 100.0, (25.0, 50.0))
st.write("rangle between",range)

color = st.select_slider("what is your favarite color?",
                         options = ["red","indgo","orange","green","blue","voilet"]
                         )
st.write("your favorite color is ",color)

start_color,end_color = st.select_slider("what is your favarite color?",
                         options = ["red","indgo","orange","green","blue","voilet"],value=["red","blue"]
                         )
st.write("your favorite color is between",start_color," and ",end_color)



import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


import pandas as pd
import streamlit as st

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(
    df,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ⭐",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
    hide_index=True,
)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")



import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data= pd.DataFrame(
    np.random.randn(20,3),
    columns= ["A","B","C"]

)
st.line_chart(chart_data)

import pandas as pd
import numpy as np 
import streamlit as st

chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=["A,","B","C"]
)
st.line_chart(chart_data)


chart_data = pd.DataFrame(
    {
        "col1" : np.random.randn(20),
        "col2" : np.random.randn(20),
        "col3" : np.random.choice(["A","B","C"],20)
    }
)
st.line_chart(chart_data,x="col1",y="col2",color="col3")


st.write("New Programm")
chart_data_01 = pd.DataFrame(
    {
        "col1" : np.random.randn(20),
        "col2" : np.random.randn(20),
        "col3" : np.random.choice(["A","B","C"],20)
    }
)
my_table = st.table(chart_data_01)

chart_data_02 = pd.DataFrame(
    {
        "col1" : np.random.randn(20),
        "col2" : np.random.randn(20),
        "col3" : np.random.choice(["A","B","C"],20)
    }
)

my_table.add_rows(chart_data_02)



import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")





