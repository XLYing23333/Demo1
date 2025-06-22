import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("Project 2")
    st.header("Introduction")
    st.write("This is a Streamlit web app that predicts the price of a house based on its features.")
    st.header("Data")
    st.write("The dataset used for this project is the Boston Housing dataset. It contains information about different features of houses in the Boston area, such as crime rate, number of rooms, etc. The dataset contains 506 rows and 14 columns.")
    st.header("Model")
    st.write("The model used for this project is a Linear Regression model. It is a simple and effective model for predicting continuous values. The model takes in the features of a house as input and outputs the predicted price of the house.")
    st.header("How to use the app")
    st.write("To use the app, simply fill in the values of the features of the house you want to predict the price for. The app will then use the Linear Regression model to predict the price and display it in a graph.")
    st.header("Conclusion")
    st.write("This project was a great learning experience for me. I learned how to use Streamlit, create a Linear Regression model, and deploy it as a web app. I also learned how to work with a real-world dataset and how to interpret the results of the model.")

if __name__ == '__main__':
    main()