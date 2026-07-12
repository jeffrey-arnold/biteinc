import streamlit as st

# MUST BE THE FIRST STREAMLIT COMMAND IN YOUR SCRIPT
st.set_page_config(page_title="My App", layout="wide")

# Updated CSS targeting modern Streamlit data-testid classes
hide_streamlit_style = """
    <style>
    /* Hides the top right toolbar button */
    div[data-testid="stToolbar"] { visibility: hidden; height: 0%; position: fixed; }
    
    /* Hides the thin colored accent line at the top */
    div[data-testid="stDecoration"] { visibility: hidden; height: 0%; position: fixed; }
    
    /* Hides the status widget spinner box */
    div[data-testid="stStatusWidget"] { visibility: hidden; height: 0%; position: fixed; }
    
    /* Hides the top menu header and the bottom footer completely */
    header { visibility: hidden; height: 0%; }
    footer { visibility: hidden; height: 0%; }
    
    /* Hides the viewer badge / GitHub icon if hosted on Community Cloud */
    .viewerBadge_link__is636, [data-testid="stViewerBadge"] { display: none !important; }
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

col1, col2 = st.columns([1, 4])

with col1:
    st.title('Bite Inc')

with col2:
    st.image("biteinc.jpg.png", width=100)

st.write('Welcome to the Bite Inc official website, where you can explore our menu, order your delicious food, and more!')

