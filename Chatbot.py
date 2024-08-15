import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the API key
genai.configure(api_key=api_key)

# Adding custom CSS with bright colors and emojis for easy identification
st.markdown("""
    <style>
        /* Main container with a bright background */
        .stApp {
            background-color: #ffeb3b; /* Bright Yellow */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Title with a bright color and emoji */
        .stMarkdown h1 {
            font-size: 36px;
            font-weight: bold;
            color: #f44336; /* Bright Red */
            margin-bottom: 20px;
            text-align: center;
        }

        /* Input prompt box with bright colors */
        .stTextInput input {
            border-radius: 5px !important;
            padding: 10px !important;
            border: 2px solid #4caf50 !important; /* Bright Green Border */
            background-color: #e1f5fe !important; /* Light Blue Background */
            color: #0d47a1 !important; /* Dark Blue Text */
            width: 100% !important;
            margin-bottom: 10px !important;
        }

        /* Button with a bright color and emoji */
        .stButton button {
            background-color: #2196f3 !important; /* Bright Blue */
            color: #ffffff !important;
            padding: 10px 20px !important;
            border: 2px solid #f57c00 !important; /* Bright Orange Border */
            border-radius: 5px !important;
            cursor: pointer !important;
        }
        .stButton button:hover {
            background-color: #ff5722 !important; /* Bright Orange on Hover */
        }

        /* Generated story section with bright background and emojis */
        .stMarkdown h2 {
            font-size: 24px;
            font-weight: bold;
            color: #8e24aa; /* Bright Purple */
            margin-top: 20px;
            text-align: center;
        }

        .stMarkdown p {
            font-size: 18px;
            line-height: 1.6;
            color: #ffffff; /* White Text */
            background-color: #c2185b; /* Bright Pink Background */
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        /* Footer text with bright color */
        .stMarkdown:last-child {
            color: #d32f2f !important; /* Bright Red Text */
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app with an emoji
st.title("🌟 AI Story Generator 🌟")

# Input prompt from the user with placeholder text
user_prompt = st.text_input("📝 Enter your prompt:", "Write a story about an AI and magic")

# Button to generate the content with an emoji
if st.button("✨ Generate Story ✨"):
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate content based on the prompt
        response = model.generate_content(user_prompt)
        
        # Display the generated content with an emoji
        st.subheader("📚 Generated Story 📚")
        st.write(response.text)
    
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")

# Additional notes or footer with an emoji
st.write("🚀 Powered by Google's Generative AI. Enter a creative prompt and let the AI do the magic!")
