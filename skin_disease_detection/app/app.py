import streamlit as st
from login_register import login_page, register_page
from feedback import feedback_page
from disease_detect import disease_page
from doctor_manage import doctor_page
from admin_panel import admin_dashboard
from utils import authenticate_user, load_cnn_model
from utils import read_users_csv, read_doctors_csv, read_feedback_csv

# Session State Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = "user"

# Sidebar Navigation
st.sidebar.title("🔬 Skin Disease Detection System")
page = st.sidebar.selectbox("Navigate to", [
    "Login", "Register", "Disease Detection", "Feedback", "Doctors", "Admin Panel"
])

# Routing based on Login Status
if not st.session_state.logged_in:
    if page == "Register":
        register_page()
    else:
        login_page()
else:
    if page == "Disease Detection":
        disease_page()
    elif page == "Feedback":
        feedback_page()
    elif page == "Doctors":
        doctor_page()
    elif page == "Admin Panel":
        if st.session_state.role == "admin":
            admin_dashboard()
        else:
            st.warning("❌ Access denied: You are not an admin.")
