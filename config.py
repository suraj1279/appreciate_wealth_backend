import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
