import streamlit as st
import google.generativeai as genai
import json

# Configure Gemini API
genai.configure(api_key="AIzaSyDkpq9waep-l3TEd-ioZ7c755baTulcAkU")

# Streamlit App Settings
st.set_page_config(page_title="Social Media Post Generator", page_icon="✨", layout="centered")
st.title("Social Media Post & Caption Generator")
st.write("Generate catchy captions, hashtags, and emojis for your social media posts using **Gen AI**!")

# User Inputs
keywords = st.text_input("Enter keywords or theme:", placeholder="e.g., Fitness, Morning workout, Motivation")
platform = st.selectbox("Select Platform:", ["Instagram", "Twitter", "LinkedIn"])

# Generate Button
if st.button("Generate Post"):
    if not keywords:
        st.warning("⚠️ Please enter some keywords first!")
    else:
        with st.spinner("Generating post... ✨"):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                prompt = f"""
                Generate a social media post for {platform} based on the keywords: {keywords}.
                Requirements:
                1. Write a catchy caption.
                2. Add 5-7 relevant hashtags.
                3. Include 3-5 emojis.
                4. Keep it engaging for the audience.
                5. Output in JSON with keys: caption, hashtags, emojis.
                """

                response = model.generate_content(prompt)
                raw_response = response.text.strip()

                # --- FIX: Remove triple backticks and language hint for JSON ---
                if raw_response.startswith("```"):
                    parts = raw_response.split("```")
                    if len(parts) >= 2:
                        raw_response = parts[1].strip()
                    # Remove "json" if present at the start
                    if raw_response.lower().startswith("json"):
                        raw_response = raw_response[4:].strip()

                # Try parsing JSON
                try:
                    result = json.loads(raw_response)

                    st.subheader("📄 Generated Caption")
                    st.write(result.get("caption", ""))

                    st.subheader("🏷️ Hashtags")
                    st.write(" ".join(result.get("hashtags", [])))

                    st.subheader("😄 Emojis")
                    st.write(" ".join(result.get("emojis", [])))

                    # Download button
                    st.download_button(
                        label="📥 Download Caption as TXT",
                        data=f"{result.get('caption', '')}\n\n{' '.join(result.get('hashtags', []))}",
                        file_name="social_media_post.txt"
                    )

                except json.JSONDecodeError:
                    st.error("⚠️ Could not parse response as JSON. Here's the raw output:")
                    st.code(response.text, language="json")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
