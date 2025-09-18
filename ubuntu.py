"""
ask user for image URL
try:
    fetch image with requests
    check if successful
    create "Fetched_Images" directory if not exists
    extract filename from URL (if none, make one up)
    open file in binary write mode
    save image
    print success message
except:
    print respectful error message
"""

import os
import requests 
from urllib.parse import urlparse
def fetch_image():
    url = input("Enter the image URL: ")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:  # If URL does not end with a filename, create one
            filename = "downloaded_image.jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # Save the image
        with open(filepath, 'wb') as file:
            file.write(response.content)

        print(f"Image successfully fetched and saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the image: {e}")
        
if __name__ == "__main__":
    fetch_image()# Each object responds differently