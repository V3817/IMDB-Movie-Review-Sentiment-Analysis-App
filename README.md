 IMDB Movie Review Sentiment Analysis App

## Overview

This Streamlit app performs sentiment analysis on IMDB movie reviews using a pre-trained Simple RNN model. It predicts whether a given movie review is positive or negative.

## Features

- **Input Review**: Accepts a movie review as input from the user.
- **Sentiment Classification**: Predicts if the sentiment of the review is positive or negative.
- **Probability Score**: Displays the confidence score for the sentiment.

## Setup Instructions

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place the pre-trained model file (`simple_rnn_imdb.h5`) in the project directory.
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## How to Use

1. Enter a movie review in the provided text area.
2. Click the "Classify" button to analyze the sentiment.
3. View the predicted sentiment and confidence score displayed below.

## Example Usage

**Input**:  
`The movie was absolutely fantastic!`

**Output**:  
- Sentiment: Positive  
- Score: 0.92  

---

Analyze movie reviews instantly and gain insights with this sentiment analysis tool! 🎥
