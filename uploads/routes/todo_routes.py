from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from models.todo_model import get_all_todos, create_todo, update_todo, delete_todo, get_todo_by_id
from utils import allowed_file
import os

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'GET':
        todos = get_all_todos()
        for todo in todos:
            todo['_id'] = str(todo['_id'])
        return jsonify(todos)

    elif request.method == 'POST':
        task = request.form.get('task')
        email = request.form.get('email')
        if not email:
            return jsonify({'message': 'Email is required!'}), 400

        file = request.files.get('image')
        todo_data = {'task': task, 'user_id': email}

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.getenv('UPLOAD_FOLDER'), filename))
            todo_data['image'] = filename

        create_todo(todo_data)
        return jsonify(todo_data), 201
@todo_bp.route('/todos/<todo_id>', methods=['PUT', 'DELETE'])
def update_delete_todo(todo_id):
    if request.method == 'DELETE':
        # No need to expect request.json in a DELETE request
        delete_todo(todo_id)
        return jsonify({'message': 'Task deleted successfully!'}), 200

    # PUT request logic remains as it is
    data = request.json
    email = data.get('email')
    todo = get_todo_by_id(todo_id, email)

    if not todo:
        return jsonify({'message': 'Todo not found or unauthorized access'}), 404

    if request.method == 'PUT':
        task = data.get('task')
        update_todo(todo_id, task)
        return jsonify({'message': 'Task updated successfully!'}), 200
