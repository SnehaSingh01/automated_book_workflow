# ai_agents/reviewer.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


def review_text(text):
    prompt = f"Review and improve the following text for clarity, grammar, and consistency:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text


