from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from . import routes                # Ensure this import is inside the app context
        app.register_blueprint(routes.bp)   # Register the blueprint

    return app
