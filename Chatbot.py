import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyC2tHTRzveUziwdv2xyPnvxvZFrhj4ZD6o")

# Title of the app
st.title("AI Story Generator")

# Input prompt from the user
user_prompt = st.text_input("Enter your prompt:", "Write a story about an AI and magic")

# Button to generate the content
if st.button("Generate Story"):
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate content based on the prompt
        response = model.generate_content(user_prompt)
        
        # Display the generated content
        st.subheader("Generated Story:")
        st.write(response.text)
    
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Additional notes or footer
st.write("Powered by Google's Generative AI. Enter a creative prompt and let the AI do the magic!")
