from flask import Blueprint

"""
    auth ->
    __name__ -> El nombre del archivo, que en este caso es __init__
    url_prefix -> Todas las rutas que empiezan por auth, seran dirigidas a este BluePrint y 
    dentro de este blueprint vamos a crear views que van a vivir en authlogin o authlogout
"""
auth = Blueprint('auth', __name__, url_prefix='/auth')

# Despues de que creamos el blueprint importemos todos los views y configuremos la aplicación
# Es importante que siempre se importe despues del auth
# el punto (.), significa que va a importar todo lo que esta en views

from . import views

