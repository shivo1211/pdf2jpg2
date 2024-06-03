from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Set the upload folder configuration
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # Ensure the upload and output directories exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'output'), exist_ok=True)

    with app.app_context():
        from . import routes  # Ensure this import is inside the app context
        app.register_blueprint(routes.bp)  # Register the blueprint

    return app
