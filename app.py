import streamlit as st
import pandas as pd
import pickle

import base64
import streamlit as st

def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{b64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call this function before app UI
set_background("imz.jpg")  # Image file must be in the same folder



# Load the trained model
with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🏡 House Price Prediction App - by Kais Khan")

# Collect input from user
area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, step=100)
bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
stories = st.selectbox("Stories", [1, 2, 3, 4])
mainroad = st.selectbox("Main Road Access", ['yes', 'no'])
guestroom = st.selectbox("Guest Room", ['yes', 'no'])
basement = st.selectbox("Basement", ['yes', 'no'])
hotwaterheating = st.selectbox("Hot Water Heating", ['yes', 'no'])
airconditioning = st.selectbox("Air Conditioning", ['yes', 'no'])
parking = st.selectbox("Parking (Number of Cars)", [0, 1, 2, 3])
prefarea = st.selectbox("Preferred Area", ['yes', 'no'])
furnishingstatus = st.selectbox("Furnishing Status", ['furnished', 'semi-furnished', 'unfurnished'])

# Create input DataFrame
input_data = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'stories': [stories],
    'mainroad': [mainroad],
    'guestroom': [guestroom],
    'basement': [basement],
    'hotwaterheating': [hotwaterheating],
    'airconditioning': [airconditioning],
    'parking': [parking],
    'prefarea': [prefarea],
    'furnishingstatus': [furnishingstatus]
})

# Predict button
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)
        st.success(f"🏠 Predicted House Price: ₹{int(prediction[0]):,}")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
