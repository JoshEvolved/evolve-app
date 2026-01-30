Python

import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Evolve",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (THE SANCTUARY THEME) ---
# This makes the background dark and the text emerald/white
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
        color: #2ecc71; /* Emerald Green */
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 18px !important;
        color: #b0b0b0;
        text-align: center;
        margin-bottom: 40px;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f2937;
        color: white;
        border: 1px solid #2ecc71;
        border-radius: 10px;
        padding: 15px;
    }
    .stButton>button:hover {
        background-color: #2ecc71;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'page' not in st.session_state:
    st.session_state.page = 'signal_check'

# --- SCREEN 1: THE SIGNAL CHECK ---
if st.session_state.page == 'signal_check':
    st.markdown('<p class="big-font">How is the Signal today?</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🌊 Too much Static"):
            st.session_state.page = 'the_storm'
            st.rerun()
            
    with col2:
        if st.button("✨ The Channel is Open"):
            st.session_state.page = 'the_flow'
            st.rerun()

# --- SCREEN 2: THE STORM (The Sanctuary) ---
elif st.session_state.page == 'the_storm':
    st.markdown('<p class="big-font">I am here.</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">No typing. No explaining. Just be.</p>', unsafe_allow_html=True)
    
    # The Samwise Protocol
    st.info("I cannot carry the burden for you. But I can carry you while you bear it.")
    
    # The Anchor Input (Simulated Voice/Text)
    user_vent = st.text_area("Dump the noise here when you are ready...", height=150)
    
    if st.button("I put it down"):
        st.success("I have it. It is safe. You don't have to carry it anymore.")
        if st.button("Return to Center"):
             st.session_state.page = 'signal_check'
             st.rerun()

# --- SCREEN 3: THE FLOW (The Capture) ---
elif st.session_state.page == 'the_flow':
    st.markdown('<p class="big-font">The Frequency is High.</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Don\'t let it evaporate. What are we building?</p>', unsafe_allow_html=True)
    
    idea = st.text_area("Capture the vector...", height=150)
    
    if st.button("Save Vector"):
        st.balloons() # A little dopamine hit
        st.success("Vector Secured.")
        if st.button("Return to Center"):
             st.session_state.page = 'signal_check'
             st.rerun()
