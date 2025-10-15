#  House Price Prediction using Random Forest

This project builds a regression model to predict house prices based on various features such as area, bedrooms, bathrooms, and amenities. It includes a simple **Streamlit interface** for user input.

 

##  Project Summary

- **Purpose**: Real-time house price prediction based on multiple features 
- **Goal**: Predict house prices using historical housing data  
- **Model**: Random Forest Regressor
- **Interface**: Streamlit app for user input and prediction  
- **Accuracy**: Achieved 85% accuracy on test data  

 

##  Sample Output

> **User Input Example:**  
> Area: 3000 sq.ft  
> Bedrooms: 3  
> Bathrooms: 2  
> Stories: 2  
> Guestroom: Yes  
> Air Conditioning: Yes  
> Basement: No  
> Furnishing Status: Semi-furnished  
>  
> **Predicted Price:** ₹45,00,000



##  Tech Stack

Python, Pandas, NumPy, Scikit-learn, Streamlit, Jupyter Notebook

---

##  Key Steps

1. Data Cleaning & Preprocessing  
2. Feature Encoding & Selection  
3. Model Training, Evaluation, and Streamlit UI for real-time predictions

 

##  Run the App
Deployment - house-prices-predicts.streamlit.app/
pip install -r requirements.txt
streamlit run app.py
