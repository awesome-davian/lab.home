# coding: utf-8
# from flask.ext.wtf import Form
from flask_login import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """Login form to access writing and settings pages"""

    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])