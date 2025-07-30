import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model

# Paths
MODEL_PATH = 'model/skin_cnn_model.h5'
USERS_CSV_PATH = 'data/users.csv'
DOCTORS_CSV_PATH = 'data/doctors.csv'
FEEDBACK_CSV_PATH = 'data/feedback.csv'

# Load CNN model
def load_cnn_model():
    try:
        model = load_model(MODEL_PATH)
        print("✅ CNN model loaded successfully!")
        return model
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None

# Read users CSV
def read_users_csv():
    try:
        return pd.read_csv(USERS_CSV_PATH)
    except Exception as e:
        print(f"❌ Error reading Users CSV: {e}")
        return pd.DataFrame()

# Read doctors CSV
def read_doctors_csv():
    try:
        return pd.read_csv(DOCTORS_CSV_PATH)
    except Exception as e:
        print(f"❌ Error reading Doctors CSV: {e}")
        return pd.DataFrame()

# Read feedback CSV
def read_feedback_csv():
    try:
        return pd.read_csv(FEEDBACK_CSV_PATH)
    except Exception as e:
        print(f"❌ Error reading Feedback CSV: {e}")
        return pd.DataFrame()

# Write users CSV
def write_users_csv(df):
    try:
        df.to_csv(USERS_CSV_PATH, index=False)
        print("✅ Users data written successfully!")
    except Exception as e:
        print(f"❌ Error writing Users CSV: {e}")

# Write doctors CSV
def write_doctors_csv(df):
    try:
        df.to_csv(DOCTORS_CSV_PATH, index=False)
        print("✅ Doctors data written successfully!")
    except Exception as e:
        print(f"❌ Error writing Doctors CSV: {e}")

# Authentication
def authenticate_user(username, password):
    users_df = read_users_csv()
    user_row = users_df[(users_df['username'] == username) & (users_df['password'] == password)]
    if not user_row.empty:
        role = user_row.iloc[0]['role']
        return True, role
    else:
        return False, None
