import streamlit as st
import pandas as pd
from utils import read_users_csv, read_doctors_csv, read_feedback_csv
from utils import write_users_csv, write_doctors_csv

def admin_dashboard():
    st.title("Admin Panel")

    tab1, tab2, tab3 = st.tabs(["Manage Users", "Manage Doctors", "View Feedback"])

    # =============== Manage Users ===============
    with tab1:
        st.header("Users Management")
        users_df = read_users_csv()
        st.dataframe(users_df, use_container_width=True)

        with st.expander("➕ Add New User"):
            new_username = st.text_input("Username")
            new_email = st.text_input("Email")
            new_password = st.text_input("Password", type="password")
            new_role = st.selectbox("Role", ["user", "admin"])
            if st.button("Add User"):
                if new_username and new_password:
                    if users_df['username'].eq(new_username).any():
                        st.error("❌ Username already exists!")
                    elif users_df['email'].eq(new_email).any():
                        st.error("❌ Email already registered!")
                    else:
                        new_user = pd.DataFrame({
                            'username': [new_username],
                            'email': [new_email],
                            'password': [new_password],
                            'role': [new_role]
                        })
                        users_df = pd.concat([users_df, new_user], ignore_index=True)
                        write_users_csv(users_df)
                        st.success("✅ User added successfully!")
                else:
                    st.error("❌ Please fill all fields!")

        with st.expander("✏️ Update/Delete User"):
            if not users_df.empty:
                selected_user = st.selectbox("Select User", users_df['username'].tolist())
                selected_user_row = users_df[users_df['username'] == selected_user].iloc[0]
                updated_password = st.text_input("Update Password", value=selected_user_row['password'], key="user_pw")
                updated_role = st.selectbox("Update Role", ["user", "admin"], index=["user", "admin"].index(selected_user_row['role']), key="user_role")

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Update User"):
                        users_df.loc[users_df['username'] == selected_user, 'password'] = updated_password
                        users_df.loc[users_df['username'] == selected_user, 'role'] = updated_role
                        write_users_csv(users_df)
                        st.success("✅ User updated successfully!")

                with col2:
                    if st.button("Delete User"):
                        users_df = users_df[users_df['username'] != selected_user]
                        write_users_csv(users_df)
                        st.success("🗑️ User deleted successfully!")

    # =============== Manage Doctors ===============
    with tab2:
        st.header("Doctors Management")
        doctors_df = read_doctors_csv()
        st.dataframe(doctors_df, use_container_width=True)

        with st.expander("➕ Add New Doctor"):
            doc_name = st.text_input("Doctor Name")
            doc_specialty = st.text_input("Specialty")
            doc_contact = st.text_input("Contact Info")
            if st.button("Add Doctor"):
                if doc_name and doc_specialty and doc_contact:
                    if doctors_df['name'].eq(doc_name).any():
                        st.error("❌ Doctor already exists!")
                    else:
                        new_doc = pd.DataFrame({
                            'name': [doc_name],
                            'specialty': [doc_specialty],
                            'contact': [doc_contact]
                        })
                        doctors_df = pd.concat([doctors_df, new_doc], ignore_index=True)
                        write_doctors_csv(doctors_df)
                        st.success("✅ Doctor added successfully!")
                else:
                    st.error("❌ Please fill all fields!")

        with st.expander("✏️ Update/Delete Doctor"):
            if not doctors_df.empty:
                selected_doc = st.selectbox("Select Doctor", doctors_df['name'].tolist())
                selected_doc_row = doctors_df[doctors_df['name'] == selected_doc].iloc[0]
                updated_specialty = st.text_input("Update Specialty", value=selected_doc_row['specialty'], key="doc_specialty")
                updated_contact = st.text_input("Update Contact", value=selected_doc_row['contact'], key="doc_contact")

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Update Doctor"):
                        doctors_df.loc[doctors_df['name'] == selected_doc, 'specialty'] = updated_specialty
                        doctors_df.loc[doctors_df['name'] == selected_doc, 'contact'] = updated_contact
                        write_doctors_csv(doctors_df)
                        st.success("✅ Doctor updated successfully!")

                with col2:
                    if st.button("Delete Doctor"):
                        doctors_df = doctors_df[doctors_df['name'] != selected_doc]
                        write_doctors_csv(doctors_df)
                        st.success("🗑️ Doctor deleted successfully!")

    # =============== View Feedback ===============
    with tab3:
        st.header("User Feedback")
        feedback_df = read_feedback_csv()
        if not feedback_df.empty:
            st.dataframe(feedback_df, use_container_width=True)
        else:
            st.info("ℹ️ No feedback submitted yet.")
