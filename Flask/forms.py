from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Submit(FlaskForm):
    data = StringField('Entre com o comando')
    submit = SubmitField('submit')