# app/feedback.py
import pandas as pd
import streamlit as st
import os

def submit_feedback(username, feedback_text):
    feedback_file = "data/feedback.csv"
    if os.path.exists(feedback_file):
        feedbacks = pd.read_csv(feedback_file)
    else:
        feedbacks = pd.DataFrame(columns=["username", "feedback"])

    new_entry = pd.DataFrame([[username, feedback_text]], columns=["username", "feedback"])
    feedbacks = pd.concat([feedbacks, new_entry], ignore_index=True)
    feedbacks.to_csv(feedback_file, index=False)

def feedback_page():
    st.subheader("Submit Feedback")
    feedback = st.text_area("Your Feedback")
    if st.button("Submit"):
        submit_feedback(st.session_state.username, feedback)
        st.success("Feedback submitted successfully!")