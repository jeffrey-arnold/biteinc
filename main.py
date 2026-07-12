import streamlit as st

# This MUST be the first Streamlit command in your app file
st.set_page_config(page_title="My App", layout="wide")

# Unified style targeting all layout modifications at once
st.markdown(
    """
    <style>
    /* 1. HIDES THE TOP RIGHT TOOLBAR STUFF */
    header { visibility: hidden !important; height: 0px !important; }
    div[data-testid="stToolbar"] { visibility: hidden !important; display: none !important; }
    div[data-testid="stDecoration"] { visibility: hidden !important; display: none !important; }
    div[data-testid="stStatusWidget"] { visibility: hidden !important; display: none !important; }
    
    /* 2. COMPLETELY REMOVES THE WATERMARK BADGE AND FOOTER ELEMENTS */
    footer { visibility: hidden !important; height: 0px !important; }
    div[data-testid="stViewerBadge"] { display: none !important; visibility: hidden !important; }
    div[class^="viewerBadge"] { display: none !important; visibility: hidden !important; }
    .viewerBadge_link__is636 { display: none !important; }
    
    /* 3. OPTIONAL: Fixes the gap at the top left by pulling content up */
    .stMainBlockContainer { padding-top: 2rem !important; }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 4])

with col1:
    st.title('Bite Inc')

with col2:
    st.image("biteinc.jpg.png", width=100)

st.write('Welcome to the Bite Inc official website, where you can explore our menu, order your delicious food, and more!')

