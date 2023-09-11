import streamlit as st
import pandas as pd
import os

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
