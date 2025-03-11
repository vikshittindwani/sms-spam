import streamlit as st
import pickle
import pandas as pandas
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def transfrom_text(text):
  ps =PorterStemmer()

  text=nltk.word_tokenize(text.lower())
  text=[i for i in text if i.isalnum()]
  text=[i for i in text if i not in stopwords.words('english')]
  text=[ps.stem(i) for i in text]

  return " ".join(text)


model=pickle.load(open('model.pkl','rb'))
tfidf=pickle.load(open('vectorizer.pkl','rb'))
st.title("SMS SPAM/NOT SPAM  classifier")
input_sms = st.text_area("enter the message")
 # 1. preprocess
if st.button('Predict'):
  transformed_sms = transfrom_text(input_sms)
 # 2. vectorize
  vector_input = tfidf.transform([transformed_sms])
  # 3. predict
  result = model.predict(vector_input)[0]
  # 4. Display
  if result == 1:
   st.header("Spam")
  else:
   st.header("Not Spam")  