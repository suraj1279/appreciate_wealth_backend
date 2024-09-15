import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.todo_routes import todo_bp
from config import Config

app = Flask(__name__)
CORS(app)

os.makedirs(os.getenv('UPLOAD_FOLDER'), exist_ok=True)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
# Load configurations
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(todo_bp)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
