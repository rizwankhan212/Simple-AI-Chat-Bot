from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


app = FastAPI()
origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allows requests from specified origins
    allow_credentials=True,           # Allows cookies and authentication headers
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allows all request headers
)
class PromptRequest(BaseModel):
    prompt:str

@app.get('/')
def home():
    return{'message':'Welcome to home page'}

@app.post('/generate')
def generate_text(request:PromptRequest):
    try:
        response = model.generate_content(request.prompt)
        return {"response": response.text}

    except ResourceExhausted:
        return {
            "response": "API quota exceeded. Please try again later."
        }

    except Exception as e:
        return {
            "response": f"Error: {str(e)}"
        }