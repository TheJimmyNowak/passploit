import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Displaying some text
st.write("Hello, welcome to this basic Streamlit app!")

# Adding a slider
slider_value = st.slider("Select a number", 0, 100)
st.write(f"You selected: {slider_value}")

# Adding a button
if st.button("Click Me"):
    st.write("You clicked the button!")

# Displaying an input text box
user_input = st.text_input("Enter your name")
if user_input:
    st.write(f"Hello, {user_input}!")

