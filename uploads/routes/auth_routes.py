from flask import Blueprint, request, jsonify
from models.user_model import find_user_by_email, create_user
from utils import logged_in_users

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if password != confirm_password:
        return jsonify({'message': 'Passwords do not match!'}), 400

    if find_user_by_email(email):
        return jsonify({'message': 'User already exists!'}), 400

    create_user(email, password)
    return jsonify({'message': 'User registered successfully!'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = find_user_by_email(email)
    if not user or user['password'] != password:
        return jsonify({'message': 'Invalid credentials'}), 400

    logged_in_users[email] = True
    return jsonify({'message': 'Login successful!', 'email': email}), 200
