import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Replace with your SerpApi API key
API_KEY = '528afad276283a7eff2416dec2a2a565559584e5e04e6e52c90be0b6c77f9900'

def search_similar_images(image_path):
    url = 'https://serpapi.com/search'
    params = {
        'engine': 'google_lens',
        'image': image_path,
        'api_key': API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

st.title("Reverse Image Search")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Convert the uploaded file to a URL
    image = Image.open(uploaded_file)
    image.save("temp_image.jpg")
    with open("temp_image.jpg", "rb") as f:
        image_data = f.read()

    # Upload the image to a hosting service (e.g., Imgur, Cloudinary) and get the URL
    # For demonstration purposes, we'll use a placeholder URL
    image_url = "https://example.com/temp_image.jpg"

    # Search for similar images
    results = search_similar_images(image_url)

    if 'image_results' in results:
        for result in results['image_results']:
            st.image(result['thumbnail'], caption=result['title'], use_column_width=True)
    else:
        st.write("No similar images found.")
