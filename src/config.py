import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Apify
APIFY_API_TOKEN = os.getenv('APIFY_API_TOKEN')

# Google Cloud Storage
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
GCS_BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')

# Etsy
ETSY_API_KEY = os.getenv('ETSY_API_KEY')

# Printify
PRINTIFY_API_TOKEN = os.getenv('PRINTIFY_API_TOKEN')

# Instagram Scraper Configuration
# Expects comma-separated full Instagram profile URLs (e.g., https://www.instagram.com/username/)
INSTAGRAM_TARGET_PROFILES = [url.strip() for url in os.getenv('INSTAGRAM_TARGET_PROFILES', '').split(',') if url.strip()]

# Computer Vision Filtering
# Comma-separated descriptive terms for the CV model to filter images by (e.g., 'sunset', 'nyc street at dusk')
CV_CONTENT_DESCRIPTIONS_FILTER = [desc.strip() for desc in os.getenv('CV_CONTENT_DESCRIPTIONS_FILTER', '').split(',') if desc.strip()]

# Basic check to ensure critical tokens are loaded
if not APIFY_API_TOKEN:
    print("Warning: APIFY_API_TOKEN not found in .env file.")

if not GOOGLE_APPLICATION_CREDENTIALS or not GCS_BUCKET_NAME:
    print("Warning: Google Cloud Storage configuration (credentials or bucket name) not found in .env file.")

# Add more checks as needed for Etsy, Printify etc.
