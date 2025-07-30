# app/doctor_manage.py
import streamlit as st
import pandas as pd
import os

def load_doctors():
    if os.path.exists("data/doctors.csv"):
        return pd.read_csv("data/doctors.csv")
    else:
        return pd.DataFrame(columns=["name", "specialty", "contact"])

def save_doctors(doctors):
    doctors.to_csv("data/doctors.csv", index=False)

def doctor_page():
    st.subheader("Manage Doctors")
    doctors = load_doctors()

    with st.form("Add Doctor"):
        name = st.text_input("Name")
        specialty = st.text_input("Specialty")
        contact = st.text_input("Contact")
        submitted = st.form_submit_button("Add Doctor")
        if submitted:
            new_doc = pd.DataFrame([[name, specialty, contact]], columns=["name", "specialty", "contact"])
            doctors = pd.concat([doctors, new_doc], ignore_index=True)
            save_doctors(doctors)
            st.success("Doctor added")

    st.dataframe(doctors)