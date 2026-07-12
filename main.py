import streamlit as st
import streamlit.components.v1 as components

# 1. Standard configurations
st.set_page_config(page_title="My App", layout="wide")

# 2. Existing working block for top-right layout and native footers
st.markdown(
    """
    <style>
    header { visibility: hidden !important; height: 0px !important; }
    div[data-testid="stToolbar"] { visibility: hidden !important; display: none !important; }
    div[data-testid="stDecoration"] { visibility: hidden !important; display: none !important; }
    footer { visibility: hidden !important; height: 0px !important; }
    .stMainBlockContainer { padding-top: 2rem !important; }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Parent DOM JavaScript injection to kill the "Hosted with Streamlit" Badge
components.html(
    """
    <script>
    function removeViewerBadge() {
        // Targets parent window elements from within the Streamlit frame
        const parentDoc = window.parent.document;
        
        // Dynamic array matching all potential deployment class signatures
        const badgeSelectors = [
            'div[data-testid="stViewerBadge"]',
            'div[class^="viewerBadge"]',
            '.viewerBadge_link__is636'
        ];
        
        badgeSelectors.forEach(selector => {
            const elements = parentDoc.querySelectorAll(selector);
            elements.forEach(el => {
                if (el) {
                    el.style.setProperty('display', 'none', 'important');
                    el.style.setProperty('visibility', 'hidden', 'important');
                    el.remove(); // Hard deletes the element from the webpage layout
                }
            });
        });
    }
    
    // Executes repeatedly to ensure the badge stays gone if Streamlit re-renders
    removeViewerBadge();
    setInterval(removeViewerBadge, 500);
    </script>
    """,
    height=0,
    width=0
)

col1, col2 = st.columns([1, 4])

with col1:
    st.title('Bite Inc')

with col2:
    st.image("biteinc.jpg.png", width=100)

st.write('Welcome to the Bite Inc official website, where you can explore our menu, order your delicious food, and more!')

