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
    if st.checkbox("Show model details"):
        st.write("The model used for this project is a Linear Regression model. It is a simple and effective model for predicting continuous values. The model is trained on the Boston Housing dataset using scikit-learn library in Python.")
    st.header("How to use the app") 
    if st.button("Check Here"):
        st.balloons()
    

if __name__ == '__main__':
    main()