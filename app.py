import streamlit as st

st.title("My first Streamlit app. It's cool! Or not.")

st.checkbox('Tick me')

if st.checkbox('Tick me to see'):
  st.write(42)


selection = st.selectbox('Choose an option', ["Nothing here", "or here", "but something here"])

if selection == "but something here":
  st.write("You found me!")
else:
  st.write("Try again")


int_val = st.slider("Pick an integer", min_value=1, max_value=10, value=5)
st.write(int_val)


float_val = st.slider("Pick a float", min_value=1.0, max_value=10.0, value=5.0, step=0.1, format="%.1f")
st.write(float_val)


st.sidebar.write("Adding text to the sidebar...")
