# app/auth.py
import pandas as pd
import streamlit as st
import os

def load_users():
    if os.path.exists("data/users.csv"):
        return pd.read_csv("data/users.csv")
    else:
        return pd.DataFrame(columns=["username", "password", "email", "role"])

def save_user(username, password, email, role="user"):
    users = load_users()
    new_user = pd.DataFrame([[username, password, email, role]], columns=["username", "password", "email", "role"])
    users = pd.concat([users, new_user], ignore_index=True)
    users.to_csv("data/users.csv", index=False)

def authenticate(username, password):
    users = load_users()
    if not users.empty:
        user = users[(users['username'] == username) & (users['password'] == password)]
        if not user.empty:
            return user.iloc[0]['role']
    return None