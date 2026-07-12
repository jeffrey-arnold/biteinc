import streamlit as st

# Ensure this is the absolute first Streamlit command
st.set_page_config(page_title="My App", layout="wide")

# Modern selector bypass targeting the dynamic hosting wrapper
st.html(
    """
    <style>
    /* Completely removes the cloud-hosted viewer watermark badge */
    div[class^="viewerBadge"], 
    div[data-testid="stViewerBadge"],
    .viewerBadge_link__is636 {
        display: none !important;
    }
    
    /* Extra fail-safe fallback to hide any old footer structures */
    footer {
        visibility: hidden !important;
        height: 0px !important;
    }
    </style>
    """
)


col1, col2 = st.columns([1, 4])

with col1:
    st.title('Bite Inc')

with col2:
    st.image("biteinc.jpg.png", width=100)

st.write('Welcome to the Bite Inc official website, where you can explore our menu, order your delicious food, and more!')

