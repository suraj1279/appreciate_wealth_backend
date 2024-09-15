import os
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient(os.getenv('MONGO_URI'))
db = client['todo_db']
todos_collection = db['todos']

def get_all_todos():
    return list(todos_collection.find())

def create_todo(todo_data):
    todos_collection.insert_one(todo_data)
    todo_data['_id'] = str(todo_data['_id'])
    return todo_data

def update_todo(todo_id, task):
    todos_collection.update_one({'_id': ObjectId(todo_id)}, {'$set': {'task': task}})

def delete_todo(todo_id):
    todos_collection.delete_one({'_id': ObjectId(todo_id)})

def get_todo_by_id(todo_id, email):
    return todos_collection.find_one({'_id': ObjectId(todo_id), 'user_id': email})
