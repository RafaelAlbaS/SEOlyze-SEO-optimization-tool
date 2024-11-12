# seo_tool.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_website_content(url):
    """Fetches HTML content from the specified URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Test fetching content
if __name__ == "__main__":
    url = "https://www.example.com"
    content = fetch_website_content(url)
    if content:
        print("Website content fetched successfully.")
    else:
        print("Failed to fetch website content.")
