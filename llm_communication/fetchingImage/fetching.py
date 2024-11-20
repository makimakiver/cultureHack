import llm_communication
import requests
from PIL import Image
from io import BytesIO

# Constants for APIs
UNSPLASH_API_KEY = ''

def array_input(input_string):
    # Remove brackets and split by commas
    items = input_string.strip("[]").split(",")
    # Clean each item and return as a list
    cleaned_items = [item.strip().strip("*").strip() for item in items]
    return cleaned_items


def fetch_images_from_unsplash(qurey):
    url = f"https://api.unsplash.com/search/photos?query={qurey}&client_id={UNSPLASH_API_KEY}"
    response = requests.get(url)
    data = response.json()
    image_urls = [item['urls']['regular'] for item in data['results'][:5]]
    return image_urls


def display_images(image_urls, query):
    # Only get the first image URL
    if image_urls:  # Check if there are any URLs
        response = requests.get(image_urls[0])  # Get only the first image
        img = Image.open(BytesIO(response.content))
        # Save with query name
        img.save(f'images/{query}_image.jpg')
    
# Example usage
input_string = get_attractions()

for query in array_input(input_string):
    image_urls = fetch_images_from_unsplash(query)
    display_images(image_urls, query)
