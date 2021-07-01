from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .config import Config
from .auth import auth
from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)


def create_app():
    app = Flask(__name__) # Nueva instancia de Flask, donde le tenemos que pasar el nombre de nuestra aplicación, que en este caso seria main.py
    bootstrap = Bootstrap(app) # Tenemos accesos de css y js de bootstrap
    
    app.config.from_object(Config) # Nos ayuda a generar nuestra llave secreta 
    
    login_manager.init_app(app)

    app.register_blueprint(auth)

    return app