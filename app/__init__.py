from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config
from .auth import auth

def create_app():
    app = Flask(__name__) # Nueva instancia de Flask, donde le tenemos que pasar el nombre de nuestra aplicación, que en este caso seria main.py
    bootstrap = Bootstrap(app) # Tenemos accesos de css y js de bootstrap
    
    app.config.from_object(Config) # Nos ayuda a generar nuestra llave secreta 
    
    app.register_blueprint(auth)

    return app