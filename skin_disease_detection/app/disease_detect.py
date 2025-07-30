# app/disease_detect.py
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load your trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("model/skin_cnn_model.h5")
    return model

model = load_model()

# Class labels for skin diseases
class_names = ['Eczema', 'Warts Molluscum and other Viral Infections', ' Melanoma', 'Atopic Dermatitis', 'Basal Cell Carcinoma', 'Melanocytic Nevi (NV)', 
                'Benign Keratosis-like Lesions (BKL)', 'Psoriasis pictures Lichen Planus and related diseases', 'Seborrheic Keratoses and other Benign Tumors', 
                'Tinea Ringworm Candidiasis and other Fungal Infections']

def predict_image(image):
    img = image.resize((224, 224))  # Resize for model
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    return predicted_class

def disease_page():
    st.subheader("Skin Disease Detection")
    uploaded_file = st.file_uploader("Upload a skin image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            result = predict_image(image)
            st.success(f"Predicted Skin Disease: **{result}**")
