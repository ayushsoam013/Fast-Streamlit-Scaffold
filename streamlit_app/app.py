import streamlit as st

st.set_page_config(
    page_title="Embeddings Optimization Admin",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Embeddings Optimization Admin")
st.markdown("""
Welcome to the administration panel for the Embeddings Optimization POC.

### Features:
- **Health Check**: Monitor the status of FastAPI, Gemini, and Qdrant.
- **Items Explorer**: Visualize items stored in Qdrant collections.

Use the sidebar to navigate between different tools.
""")

st.sidebar.success("Select a tool above.")
