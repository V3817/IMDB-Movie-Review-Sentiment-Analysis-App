import streamlit as st 
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb

word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

model=load_model("simple_rnn_imdb.h5")

def decode_review(encoded_review):
  return " ".join([reverse_word_index.get(i - 3, "?") for i in encoded_review])

def preprocess_text(text):
  words=text.lower().split()
  encoded_review=[word_index.get(word,2)+3 for word in words]
  padded_review=sequence.pad_sequences([encoded_review],maxlen=500)
  return padded_review

def predict_sentiment(review):
  preprocessed_input=preprocess_text(review)
  prediction=model.predict(preprocessed_input)
  sentiment="Positive" if prediction[0][0] >0.5 else "Negative"
  return sentiment ,prediction[0][0]

st.title("IMDB Movie Review Sentiment Analysis")
st.write("Write a movie review to predict sentiment analysis")

user_input =st.text_area("Movie Review")
if st.button("Classify"):
  preprocessed_input=preprocess_text(user_input)

  prediction=model.predict(preprocessed_input)
  sentiment="Positive" if prediction[0][0] >0.5 else "Negative"

  st.write(f"review:{user_input}")
  st.write(f"sentiment:{sentiment}")
  st.write(f"score:{prediction[0][0]}")

else:
  st.write("Please enter the movie review ")

