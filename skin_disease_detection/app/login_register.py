# app/login_register.py
import streamlit as st
from auth import authenticate, save_user

def login_page():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        role = authenticate(username, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = role
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid credentials")

def register_page():
    st.subheader("Register")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        save_user(username, password, email)
        st.success("Registration successful. Please log in.")