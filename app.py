import streamlit as st
import pandas as pd

# Load the dataset from GitHub (replace with your raw CSV URL)
csv_url = "https://raw.githubusercontent.com/MK316/stress2024/refs/heads/main/data/stressdata1.csv"
df = pd.read_csv(csv_url)

# Set up the Streamlit interface
st.title("📚 Word Search Application")

# User input for searching a word
user_input = st.text_input("Enter a word to search:", placeholder="Type a word here...")

# Search functionality
if user_input:
    # Check if the word exists in the 'Word' column
    result = df[df['Word'].str.lower() == user_input.lower()]
    if result.empty:
        st.error("The word is not in the list.")
    else:
        # Extract details for the word
        pos = result.iloc[0]['POS']
        stress = result.iloc[0]['Stress']
        transcription = result.iloc[0]['Transcription']

        # Display the results in a flashcard style
        st.markdown(f"<div style='font-size: 16px; padding: 10px; border: 2px solid #4CAF50; border-radius: 5px;'>"
                    f"<strong>POS:</strong> {pos}<br>"
                    f"<strong>Stress:</strong> {stress}<br>"
                    f"<strong>Transcription:</strong> {transcription}"
                    f"</div>", unsafe_allow_html=True)
