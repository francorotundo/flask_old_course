from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .auth import auth
def create_app():
    app = Flask(
    __name__,
    template_folder='./templates', 
    static_folder='./static'
    )

    bootstrap = Bootstrap(app)

    app.config.from_object(Config)
    
    app.register_blueprint(auth)
    
    return app