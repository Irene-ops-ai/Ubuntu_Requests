Ubuntu Image Fetcher
A Python tool for mindfully collecting images from the web, inspired by Ubuntu principles of Community, Respect, Sharing, and Practicality.

📌 Features

Prompt user for one or more image URLs.

Create a Fetched_Images directory if it doesn’t exist.

Download and save images with meaningful filenames.

Verify that the URL points to an actual image (Content-Type).

Prevent duplicate downloads by checking image hashes.

Handle errors gracefully (invalid URLs, connection issues, timeouts).

🚀 Usage
1. Clone / Download the Script

Place the Python file (e.g., ubuntu_image_fetcher.py) into your working folder.

2. Run the Script
python ubuntu_image_fetcher.py

3. Example Terminal Output
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (comma-separated): https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.

⚙️ Requirements

Python 3.8+ (tested on Python 3.13.5)

Install dependencies:

pip install requests

🔒 Precautions

Always ensure you trust the source before downloading files.

The program checks HTTP headers to confirm the file is an image.

Duplicate prevention ensures storage space is not wasted.

🌍 Ubuntu Principles in Action

Community → Connects to the wider web to fetch and share images.

Respect → Graceful error handling ensures a smooth experience.

Sharing → Stores files neatly in a common directory for reuse.

Practicality → Simple, real-world tool for managing image downloads.

📝 Challenge Extensions

Support for multiple URLs (implemented ✅).

Skip non-image files (implemented ✅).

Prevent duplicate downloads (implemented ✅).

Add checks for important HTTP headers like Content-Type (implemented ✅).


✅ This project demonstrates practical coding, ethical design, and Ubuntu values.
