import requests
import os
from urllib.parse import urlparse
from datetime import datetime
import hashlib

def sanitize_filename(filename):
    """Ensure filename is safe for saving."""
    return "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_', '-')).rstrip()

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs from user (comma-separated)
    urls = input("Please enter one or more image URLs (comma-separated): ").split(",")

    # Create directory if it doesn't exist
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    # Track downloaded hashes to prevent duplicates
    downloaded_hashes = set()

    for url in [u.strip() for u in urls if u.strip()]:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # --- Precaution: Check headers ---
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipped (not an image): {url}")
                continue

            # Extract filename
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

            filename = sanitize_filename(filename)
            filepath = os.path.join(folder, filename)

            # --- Duplicate prevention: check hash ---
            file_hash = hashlib.md5(response.content).hexdigest()
            if file_hash in downloaded_hashes:
                print(f"✗ Skipped duplicate: {filename}")
                continue
            downloaded_hashes.add(file_hash)

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

if __name__ == "__main__":
    main()
