from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Set the upload folder configuration
    app.config['UPLOAD_FOLDER'] = 'uploads'  # You can change 'uploads' to any directory you prefer

    with app.app_context():
        from . import routes  # Ensure this import is inside the app context
        app.register_blueprint(routes.bp)  # Register the blueprint

    return app
