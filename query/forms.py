from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField
from wtforms import StringField

class Form(FlaskForm):
    username = StringField("Username")
    captcha = RecaptchaField()