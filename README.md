# SMS Spam Classifier

## Overview
This project is an **# SMS Spam Classifier** built using Jupyter Notebook for model development and Streamlit for an interactive web application. It helps classify SMS messages as **# Spam** or **# Ham (Not Spam)** using Natural Language Processing (NLP) and Machine Learning.

## Features
- **# Text Preprocessing:** Cleans and tokenizes SMS messages.
- **# Machine Learning Models:** Uses algorithms like Naïve Bayes, Logistic Regression, or LSTM for classification.
- **# Interactive UI with Streamlit:** Allows users to enter messages and get real-time predictions.
- **# Accuracy Metrics:** Displays precision, recall, and F1-score.
- **# Data Visualization:** Shows word clouds and spam vs. ham statistics.

## Installation
### Prerequisites
Ensure Python is installed. Install dependencies using:
```bash
pip install pandas numpy scikit-learn nltk streamlit wordcloud
```

### Clone the Repository
```bash
git clone https://github.com/vikshittindwani/sms-spam
cd sms-spam-classifier
```

## Usage
### 1. Model Development (Jupyter Notebook)
- Open `SMS_Spam_Classifier.ipynb` in Jupyter Notebook.
- Run the cells to preprocess data, train models, and evaluate performance.

### 2. Running the Streamlit App
To launch the web interface, run:
```bash
streamlit run app.py
```
Then open the **# localhost URL** in your browser.

## Project Structure
```
sms-spam-classifier/
│── data/                   # Dataset files (CSV, JSON, etc.)
│── notebooks/              # Jupyter Notebook for model development
│── app.py                  # Streamlit application
│── model.py                # Classification logic
│── requirements.txt        # Dependencies
│── README.md               # Documentation
```

## Dataset
The dataset used is the **# SMS Spam Collection** dataset, containing labeled SMS messages for spam detection.

## Screenshots
### NoteBook
(![image](https://github.com/user-attachments/assets/70312f98-491e-4ea6-a2df-997b8de1557b)



## Future Enhancements
- Improve classification with **# Deep Learning (LSTMs, Transformers)**.
- Implement **# real-time SMS filtering**.
- Deploy on **# Heroku/AWS**.

## Contributing
Fork the repository and submit pull requests to contribute.

## License
This project is licensed under the **# MIT License**.

---
### Stay Safe from Spam! 📩🚀

