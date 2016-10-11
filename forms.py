from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

class CustomerLoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password',
                             validators=[DataRequired(),
                                         Length(min=6, message='Password should be at least 6 characters long')])
