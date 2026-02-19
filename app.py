import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use stable model
model = genai.GenerativeModel("gemini-3-flash-preview")

st.set_page_config(page_title="VidhyaGuide AI", page_icon="🎓")

st.title("🎓 VidhyaGuide AI - Career Planning & Resume Mentor")
st.write("Paste your resume below and get AI-powered career guidance.")

resume = st.text_area("📄 Paste Your Resume Here", height=250)

if st.button("🚀 Analyze Resume"):
    if resume.strip() == "":
        st.warning("Please paste your resume first.")
    else:
        with st.spinner("Analyzing with AI..."):
            try:
                prompt = f"""
                You are an expert AI Career Mentor.

                Analyze this resume and provide:

                1. Extracted Skills
                2. Strengths
                3. Areas for Improvement
                4. Skill Score out of 10
                5. Top 3 Career Recommendations
                6. 3-Month Learning Roadmap

                Resume:
                {resume}
                """

                response = model.generate_content(prompt)

                st.success("✅ Analysis Complete!")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {str(e)}")
