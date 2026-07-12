
import streamlit as st

st.set_page_config(page_title="My App", layout="wide")

# This hides the footer watermark and the top-right hamburger menu completely
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


col1, col2 = st.columns([1, 4])

with col1:
    st.title('Bite Inc')

with col2:
    st.image("biteinc.jpg.png", width=100)

st.write('Welcome to the Bite Inc official website, where you can explore our menu, order your delicious food, and more!')

