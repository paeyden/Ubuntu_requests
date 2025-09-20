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

import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs
    urls = input("Enter image URLs separated by commas: ").split(",")

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        url = url.strip()
        if not url:
            continue  # skip empty entries

        try:
            headers = {"User-Agent": "UbuntuFetcher/1.0 (Respectful Image Fetcher)"}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

            # Check content type
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipping {url} — not an image (Content-Type: {content_type})")
                continue

            # Extract filename
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = "downloaded_image.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            # Prevent duplicates
            if os.path.exists(filepath):
                print(f"⚠️ Skipping {filename} — already exists.")
                continue

            # Save the image
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("\nConnection strengthened. Community enriched.")
    print("Remember: 'I am because we are.'")

if __name__ == "__main__":
    main()
