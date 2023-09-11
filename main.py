import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.header("This is my widgets page :umbrella_with_rain_drops:")
button1 = st.button("This is my button ")
st.write("Look here=", button1)

data = pd.read_csv("data/tips.csv")


def display_random(df):
    return df.sample(6)


new_button = st.button("Show me 6 rows from my data")
if new_button:
    sample = display_random(data)
    st.dataframe(sample)

yes = st.checkbox("I agree with conditions")
st.write("Your selection is: ", yes)

st.markdown("---")
st.subheader("My Radio Button")

results = st.radio("Which team you hates more?", ("Real Madrid", "Manchester City", "Barcelona"))
st.write("You hate: ", results)

st.markdown("------")
st.subheader("Create a select box")
my_box = st.multiselect("your favourite classes",
                        ["ML2", "Python2", "All Conchita Classes"])
st.write("You select: ", my_box)

st.markdown("-----")
st.subheader("Our first slider")
grade = st.slider("My score for ml2 will be: ", 0, 10, 1)
st.write("Your score will be: ", grade)

st.markdown("----")
st.subheader("My first form")
name = st.text_input("Tell us your name")
age = st.number_input("Tell us your age")
describe = st.text_area(height=150, label="Tell us about your expectations")
dob = st.date_input("Tell us your date of birth:")

st.markdown("-----")
st.subheader("How to upload the file")
your_file = st.file_uploader("Upload the file")
save_button = st.button("Save File")
if save_button:
    if your_file is not None:
        with open(os.path.join("./uploads", your_file.name), mode="wb") as f:
            f.write(your_file.getbuffer())
            st.success("Your File is upload ok")
    else:
        st.error("Please select a file to upload")

folder_path = '/path/to/folder'
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
st.subheader("Files:")
for file in files:
    st.write(file)

st.header("First Interactive Plots")
my_data = pd.DataFrame(np.random.randint(low=1, high=25, size=(6, 4)), columns=["a","b","c","d"])
st.write(my_data)

st.bar_chart(my_data)
st.line_chart(my_data)
st.area_chart(my_data)

st.markdown("----")
st.header("Load a real dataframe")
tips_data = pd.read_csv("./data/tips.csv")
st.header("Distribution Chart")

my_selection = st.selectbox("Select the category to color", ("sex", "smoker", "day", "time"))
st.write(my_selection)
fig = px.histogram(data_frame=tips_data, x="total_bill", color=my_selection)
st.plotly_chart(fig)

st.markdown("----")
st.subheader("Scatter plot")
my_selection2 = st.selectbox("Select the category to color on scatter", ("sex", "smoker", "day", "time"))
st.write(my_selection2)
fig = px.scatter(data_frame=tips_data, x="total_bill", y="tip", color=my_selection2)
st.plotly_chart(fig)

st.markdown("----")
st.subheader("My last plot")
path = st.multiselect("Features to plot", ("sex", "smoker", "day", "time"))
fig = px.sunburst(data_frame=tips_data, path=path)
st.plotly_chart(fig)