from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()]) # Inicializamos instancia de DataRequired
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


class TodoForm(FlaskForm):
    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Crear')


class DeleteForm(FlaskForm):
    submit = SubmitField('Borrar')

class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualizar')