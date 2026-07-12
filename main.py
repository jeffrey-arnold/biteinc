import streamlit as st

st.markdown("""
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 10])

with col1:
    st.title('Bite Inc')

with col2:
    st.image("biteinc.jpg.png", width=100)

st.write('Welcome to the Bite Inc official website, where you can explore our menu, order your delicious food, and more!')

