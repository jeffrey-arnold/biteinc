import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

# Hide watermark with CSS
st.markdown("""
    <style>
        .stAppViewContainer footer {display: none;}
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])

with col1:
    st.title('Bite Inc')

with col2:
    st.image("biteinc.jpg.png", width=100)  # Relative path!

st.write('Welcome to the Bite Inc official website, where you can explore our menu, order your delicious food, and more!')
