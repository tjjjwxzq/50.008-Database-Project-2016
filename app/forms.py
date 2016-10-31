from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from app.validators import RecordExists, NoDuplicateRecord
from app.models import Customer, StoreManager

class CustomerLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   RecordExists(Customer, 'username')])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=6, message='Password should be at least 6 characters long')])

class CustomerSignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   NoDuplicateRecord(Customer, 'username')])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    credit_card_number = StringField('Credit Card Number', validators=[DataRequired(),
                                                                       Length(min=10, max=19)])
    address = StringField('Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                   Length(min=6, message='Password should be at least 6 characters long')])
    password_confirmation = PasswordField('Password Confirmation', validators=[DataRequired(),
                                                                             Length(min=6, message='Password should be at least 6 characters long'),
                                                                             EqualTo('password', message='Passwords must match')])

class StoreManagerLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   RecordExists(StoreManager, 'username')])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=6, message='Password should be at least 6 characters long')])
