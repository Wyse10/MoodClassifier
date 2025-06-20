# 📊 Sentiment Analysis Tool

This is a project built with FastAPI for the backend and HTML/CSS for the frontend. It predicts whether a given text has **positive** or **negative** sentiment.

## Features
- Analyze custom text (e.g., movie reviews)
- Predict sentiment using Logistic Regression
- Preprocess text using TF-IDF vectorizer
- User-friendly web interface
- Easily expandable to BERT or other ML models

## Tech Stack
### Machine Learning & NLP
- Python
- Scikit-learn
- Pandas
- NLTK
- TfidfVectorizer

### Backend
- FastAPI
- Pydantic
- Joblib (for loading models)

## Frontend
- HTML
- CSS

## 📂 Project Structure
.
├── main.py
|── data/
│   └── IMDB_Dataset.csv
├── model/
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
|── notebooks/
│   └── sentiment_analysis.ipynb
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── README.md
└── .gitignore

## Install dependencies
pip install -r requirements.txt

## Run the FastAPI app
uvicorn app.main:app --reload

## Run the Project

1. Clone the repo:
```bash
git clone https://github.com/Wyse10/MoodClassifier.git

## 📊 Author
Solomon Monne

Happy Coding ✨
