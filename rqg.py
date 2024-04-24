import streamlit as st
import requests
from PIL import Image
import random

# Dictionary of themes with their corresponding keywords for API
themes = {
    "Wisdom": "wisdom",
    "Humor": "humor",
    "Love": "love",
    "Life": "life",
    "Motivation": "inspirational",
    "Success": "success",
    "Happiness": "happiness",
    "Art": "art",
}

# Function to fetch a random quote based on the theme
def fetch_quote(theme):
    url = f"https://api.quotable.io/random?tags={theme}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["content"], data["author"]
    else:
        return "Error fetching quote", "Unknown"

# Function to load a random background image related to the theme
def load_random_background(theme):
    url = f"https://source.unsplash.com/800x600/?{theme}"
    image = Image.open(requests.get(url, stream=True).raw)
    return image

def main():
    st.title("Wisdom Generator")
    st.header("Get Inspired!")

    # Theme selection
    selected_theme = st.selectbox("Select Theme", list(themes.keys()))

    # Customization options
    background_color = st.color_picker("Choose Background Color", "#f0f0f0")
    font_color = st.color_picker("Choose Font Color", "#333333")
    font_size = st.slider("Select Font Size", min_value=12, max_value=36, value=20)

    if st.button("Generate Quote"):
        quote, author = fetch_quote(themes[selected_theme])
        background_image = load_random_background(themes[selected_theme])

        st.markdown(f'<div style="background-color: {background_color}; padding: 20px; border-radius: 10px;">', unsafe_allow_html=True)
        st.image(background_image, use_column_width=True)
        st.markdown(f'<p style="color: {font_color}; font-size: {font_size}px;">"{quote}"</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: {font_color}; font-size: {font_size - 4}px;">- *{author}*</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.write("---")  # Add a separator between quotes

if __name__ == "__main__":
    main()


