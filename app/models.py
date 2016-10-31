# pylint: disable=invalid-name
# pylint: disable=too-many-arguments

from app import db
from sqlalchemy.dialects.postgresql import ARRAY
from flask_login import UserMixin

class Customer(db.Model, UserMixin):

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    credit_card_number = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)

    def __init__(self, username, password, first_name, last_name, credit_card_number, address):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.credit_card_number = credit_card_number
        self.address = address

    def __repr__(self):
        return 'Customer {}'.format(self.username)

    # for flask-login
    def get_id(self):
        return self.username

    def verify_password(self, password):
        return self.password == password
