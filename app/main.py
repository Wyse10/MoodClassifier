from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib

# Load model and vectorizer
model = joblib.load("C:/Users/Solowyse/Desktop/APP/model/sentiment_model.pkl")
vectorizer = joblib.load("C:/Users/Solowyse/Desktop/APP/model/vectorizer.pkl")

# FastAPI app
app = FastAPI()

# Set up templates and static directories
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Homepage
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API route
class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(input: TextInput):
    vec = vectorizer.transform([input.text])
    prediction = model.predict(vec)[0]
    sentiment = "Positive" if prediction == 1 else "Negative"
    return {"sentiment": sentiment}