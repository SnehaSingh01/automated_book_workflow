import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()

for m in models:
    print(f"Model: {m.name}, Supports generate_content: {'generateContent' in m.supported_generation_methods}")
