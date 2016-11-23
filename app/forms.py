from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, DecimalField, SelectField, HiddenField, RadioField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo, Regexp, NumberRange
from app.validators import RecordExists, NoDuplicateRecord
from app.models import Customer, StoreManager, Book

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

class NewBookForm(FlaskForm):
    ISBN = StringField('ISBN', validators=[DataRequired(),
                                           Length(min=13,max=13, message='ISBN should be 13 numbers long'),
                                           Regexp(r'\d{13}', message='ISBN should consist only of numeric characters'),
                                           NoDuplicateRecord(Book, 'ISBN')])
    title = StringField('Title', validators=[DataRequired()])
    authors = StringField('Authors', validators=[DataRequired()])
    publisher = StringField('Publisher', validators=[DataRequired()])
    year_of_publication = IntegerField('Year of Publication', validators=[DataRequired(),
                                                                         NumberRange(min=1900, max=3000, message='Publication year should be a valid year')])
    stock = IntegerField('Stock', validators=[InputRequired(),
                                              NumberRange(min=0, message='Stock should be a valid number')])
    price = DecimalField('Price', validators=[DataRequired(),
                                              NumberRange(min=0, message='Price should be a valid number')])
    format = SelectField('Format', choices=[('hardcover', 'Hardcover'), ('softcover', 'Softcover')])
    subject = StringField('Subject', validators=[DataRequired()])
    keywords = StringField('Keywords', validators=[DataRequired()])

class EditBookForm(FlaskForm):
    ISBN = StringField('ISBN', validators=[DataRequired(),
                                           Length(min=13,max=13, message='ISBN should be 13 numbers long'),
                                           Regexp(r'\d{13}', message='ISBN should consist only of numeric characters')])
    title = StringField('Title', validators=[DataRequired()])
    authors = StringField('Authors', validators=[DataRequired()])
    publisher = StringField('Publisher', validators=[DataRequired()])
    year_of_publication = IntegerField('Year of Publication', validators=[DataRequired(),
                                                                         NumberRange(min=1900, max=3000, message='Publication year should be a valid year')])
    stock = IntegerField('Stock', validators=[InputRequired(),
                                              NumberRange(min=0, message='Stock should be a valid number')])
    price = DecimalField('Price', validators=[DataRequired(),
                                              NumberRange(min=0, message='Price should be a valid number')])
    format = SelectField('Format', choices=[('hardcover', 'Hardcover'), ('softcover', 'Softcover')])
    subject = StringField('Subject', validators=[DataRequired()])
    keywords = StringField('Keywords', validators=[DataRequired()])

class FilterBooksForm(FlaskForm):
    authors = StringField('Authors')
    publisher = StringField('Publisher')
    title = StringField('Title')
    subject = StringField('Subject')

class CreateReviewForm(FlaskForm):
    score = IntegerField('Score', validators=[DataRequired(),
                                              NumberRange(min=0,max=10,message='Number should be between 0 to 10')])
    description = StringField('Description')

class AddBookToOrderForm(FlaskForm):
    isbn = HiddenField()
    quantity = IntegerField('Quantity', validators=[DataRequired()])

class CreateFeedbackForm(FlaskForm):
    rating = RadioField('Rating', choices=[('0','Not Useful'),('1','Useful'), ('2', 'Very Useful')])

class StatisticsForm(FlaskForm):
    month = SelectField('Month', coerce=int, choices=[
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    ])
    number = IntegerField('Number')
