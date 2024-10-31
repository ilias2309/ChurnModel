# Churn Prediction Platform

This repository contains a churn prediction platform developed using Streamlit. The platform is designed to predict customer churn using a machine learning model developed in-house. The aim is to provide a simple yet effective tool for businesses to identify customers who are likely to leave and take proactive measures to retain them.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Model Details](#model-details)
7. [WebAppImages](#WebAppImages)


## Project Overview

Customer churn is a significant issue for many businesses, and predicting churn can help companies take preventive actions. This project provides a web-based platform for predicting customer churn using a machine learning model. The platform is built using Streamlit, a popular Python framework for creating web applications with ease.

## Features

- **User-Friendly Interface**: A simple and intuitive web interface built with Streamlit.
- **Real-Time Predictions**: Make predictions on customer churn in real-time.
- **Customizable Model**: Use a pre-trained model or integrate your own model for churn prediction.
- **Visualization**: Visualize the input data and prediction results.

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the web interface.
- **Scikit-learn**: For model development and evaluation.
- **Pandas**: For data manipulation.
- **NumPy**: For numerical computations.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone [URL]
    cd Churn-Web-App
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**:

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Launch the application**: Open your web browser and navigate to `http://localhost:8501` (or the specified URL in the terminal).
2. **Upload Data**: Use the provided interface to upload your customer data for prediction.
3. **View Predictions**: The platform will display the churn prediction results along with relevant visualizations.

## Model Details

The churn prediction model is developed using a machine learning approach. It takes customer data as input and outputs the probability of churn. The model is trained on historical customer data, which includes features such as customer demographics, usage patterns, and interaction history.

- **Model Type**: Xgboost ,Logistic Regression, Random Forest, etc.
- **Training Data**: A csv file that contain data abot costimers.
- **Performance Metrics**: List performance metrics such as accuracy, precision, recall, F1-score

## WebAppImages


see WebAppImages Folder