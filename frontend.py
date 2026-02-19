if st.button("🚀 Analyze Resume"):
    if resume.strip() == "":
        st.warning("Please paste your resume first.")
    else:
        with st.spinner("Analyzing with AI..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json={"resume_text": resume},
                    timeout=30
                )

                st.write("Status Code:", response.status_code)
                st.write("Raw Response:", response.text)

                if response.status_code == 200:
                    result = response.json().get("result", "No result returned")
                    st.success("✅ Analysis Complete!")
                    st.write(result)
                else:
                    st.error("Backend error occurred")

            except Exception as e:
                st.error(f"Error: {str(e)}")
