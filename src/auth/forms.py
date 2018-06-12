from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators


class LoginForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField('username', validators=[validators.DataRequired(), validators.Length(min=6, max=120)])
    password = StringField('password', validators=[validators.DataRequired()])