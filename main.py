import streamlit as st
from home import show_home_page  # Import your home page function
from dashboard import show_dashboard  # Import your dashboard function

# Page configuration
st.set_page_config(
    page_title="Crop Monitoring System",
    page_icon="🌱",
    layout="wide"
)

# Initialize session state for page navigation
# Use 'current_page' to match what home.py expects
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Also initialize page for backward compatibility
if 'page' not in st.session_state:
    st.session_state.page = "home"

# Navigation logic
def main():
    # Check both session state variables for navigation
    current_page = st.session_state.get('current_page', 'Home')
    page = st.session_state.get('page', 'home')
    
    # Normalize page names and navigate accordingly
    if current_page == "Dashboard" or page == "dashboard":
        show_dashboard()
    else:  # Default to home page
        show_home_page()

if __name__ == "__main__":
    main()