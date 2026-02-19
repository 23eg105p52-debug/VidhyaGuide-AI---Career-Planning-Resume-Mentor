from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use model compatible with your version
model = genai.GenerativeModel("gemini-pro")

app = FastAPI()

class ResumeRequest(BaseModel):
    resume_text: str

@app.post("/analyze")
def analyze_resume(request: ResumeRequest):
    prompt = f"""
    You are an expert AI Career Mentor.

    Analyze this resume and provide:

    1. Extracted Skills
    2. Strengths
    3. Areas for Improvement
    4. Skill Score out of 10
    5. Top 3 Career Recommendations with reasons
    6. 3-Month Learning Roadmap

    Resume:
    {request.resume_text}
    """

    response = model.generate_content(prompt)

    return {"result": response.text}
