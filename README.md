# Sentiment Analysis Web App

This project is a sentiment analysis web application that predicts the sentiment of a given text as Positive, Neutral, or Negative. The application leverages a logistic regression model trained on the Sentiment140 dataset and provides a user-friendly web interface for inputting text and displaying predictions.

## Project Description

The Sentiment Analysis Web App is designed to help users understand the sentiment expressed in text data, such as tweets or reviews. By analyzing the text, the app determines whether the sentiment is positive, neutral, or negative. This can be useful for businesses to monitor customer feedback, social media sentiment, and more.

### Key Features

- **Data Cleaning and Preprocessing:** The text data undergoes a thorough cleaning process, including removing mentions, URLs, HTML entities, punctuations, numbers, and stopwords. The cleaned text is then lemmatized to ensure better analysis.
- **TF-IDF Vectorization:** The cleaned text is transformed into numerical features using TF-IDF vectorization, which helps in capturing the importance of words in the text.
- **Logistic Regression Model:** A logistic regression model is trained on the vectorized text data to predict sentiment with high accuracy.
- **Flask Web Interface:** A simple and intuitive web interface built with Flask allows users to input text and view sentiment predictions in real-time.

## Installation



1. **Download the Sentiment140 dataset:**

    Download the dataset from [Kaggle](https://www.kaggle.com/datasets/kazanova/sentiment140) and place the `sentiment140.csv` file in the project directory.

## Usage

1. **Preprocess and Train the Model:**

    Run the provided scripts to preprocess the data and train the logistic regression model. This will generate the model and vectorizer files needed for the web app.

    ```bash
    python preprocess.py
    python train_model.py
    ```

2. **Run the Flask Application:**

    Start the Flask web server to use the web interface.

    ```bash
    python app.py
    ```

3. **Access the Web App:**

    Open your web browser and go to `http://127.0.0.1:5000` to use the sentiment analysis web app.


## Model Training

The `train_model.py` script handles the training of the logistic regression model. It involves the following steps:

1. **Loading and Cleaning Data:** The Sentiment140 dataset is loaded and unnecessary columns are removed.
2. **Preprocessing Text:** The text data is cleaned using various preprocessing techniques.
3. **Vectorization:** The cleaned text is converted into numerical features using TF-IDF vectorization.
4. **Training the Model:** The logistic regression model is trained on the vectorized data.
5. **Saving the Model:** The trained model and vectorizer are saved for later use in the web app.

## Model Persistence

The trained model and vectorizer are saved using `joblib` for efficient loading and prediction during runtime. The files are stored in the `model` directory.

## Running the Web App

The `app.py` script initializes and runs the Flask web server. It provides an interface for users to input text and receive sentiment predictions.

## video


https://github.com/AshrafGamalG3/Sentiment-Analysis/assets/159867026/868b4ac8-b9b1-470b-a480-ae57f559c8ae




