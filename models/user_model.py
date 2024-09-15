import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client['todo_db']
users_collection = db['users']

def find_user_by_email(email):
    return users_collection.find_one({'email': email})

def create_user(email, password):
    users_collection.insert_one({'email': email, 'password': password})
