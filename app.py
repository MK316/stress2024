import streamlit as st
import pandas as pd

# Load the dataset from GitHub
csv_url = "https://raw.githubusercontent.com/MK316/stress2024/refs/heads/main/data/stressdata1.csv"
df = pd.read_csv(csv_url)

# POS mapping for full form
pos_mapping = {
    "n": "Noun",
    "adj": "Adjective",
    "v": "Verb",
    "adv": "Adverb"
}

def convert_pos(pos_abbreviations):
    """Convert POS abbreviations to full forms."""
    pos_list = [pos_mapping[abbreviation.strip()] for abbreviation in pos_abbreviations.split(",") if abbreviation.strip() in pos_mapping]
    return ", ".join(pos_list)

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
        full_pos = convert_pos(pos)
        stress = result.iloc[0]['Stress']
        transcription = result.iloc[0]['Transcription']

        # Display the results in a flashcard style
        st.markdown(f"<div style='font-size: 24px; padding: 10px; border: 2px solid #4CAF50; border-radius: 5px;'>"
                    f"<strong>POS:</strong> {full_pos}<br>"
                    f"<strong>Stress:</strong> {stress}<br>"
                    f"<strong>Transcription:</strong> {transcription}"
                    f"</div>", unsafe_allow_html=True)
