# ai_agents/writer.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


def spin_text(text):
    prompt = f"Rewrite the following chapter text in a more engaging and polished narrative style:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text



