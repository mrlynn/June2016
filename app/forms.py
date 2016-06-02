from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """Login form to access writing and settings pages"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])

class SettingsForm(Form):
    """Settings form to access writing and settings pages"""

    accesskey = StringField('Access Key', validators=[DataRequired()])
    accesssecret = StringField('Access Token', validators=[DataRequired()])
    consumerkey = StringField('Consumer Key', validators=[DataRequired()])
    consumersecret = StringField('Consumer Secret', validators=[DataRequired()])
