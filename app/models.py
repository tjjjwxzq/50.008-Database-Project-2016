# pylint: disable=invalid-name
# pylint: disable=too-many-arguments

from app import db
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy.schema import CheckConstraint
from flask_login import UserMixin
from inflection import humanize

class Customer(db.Model, UserMixin):

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String(), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    credit_card_number = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    reviews = db.relationship('Review',
                              backref=db.backref('customer', lazy='joined'),
                              lazy='dynamic'
                             )
    orders = db.relationship('Order',
                             backref=db.backref('customer', lazy='joined'),
                             lazy='dynamic'
                            )

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

    def order_in_progress(self):
        return self.orders.filter_by(status='in_progress').first()

class StoreManager(db.Model):

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return 'Store Manager {}'.format(self.username)

    def get_id(self):
        return self.username

    def verify_password(self, password):
        return self.password == password

class Book(db.Model):

    formats = ['hardcover', 'softcover']

    ISBN = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    authors = db.Column(ARRAY(db.String()), nullable=False)
    publisher = db.Column(db.String(), nullable=False)
    year_of_publication = db.Column(db.SmallInteger(), nullable=False)
    stock = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Numeric(), nullable=False)
    format = db.Column(db.Enum('hardcover', 'softcover', name='formats'), nullable=False)
    subject = db.Column(db.String(), nullable=False)
    keywords = db.Column(ARRAY(db.String()), nullable=False)
    reviews = db.relationship('Review',
                              backref=db.backref('book', lazy='joined'),
                              lazy='dynamic'
                             )

    def __init__(self, **kwargs):
        self.ISBN = kwargs['ISBN']
        self.title = kwargs['title']
        self.authors = kwargs['authors']
        self.publisher = kwargs['publisher']
        self.year_of_publication = kwargs['year_of_publication']
        self.stock = kwargs['stock']
        self.price = kwargs['price']
        self.format = kwargs['format']
        self.subject = kwargs['subject']
        self.keywords = kwargs['keywords']

    def __repr__(self):
        return '{} ISBN: {}'.format(self.title, self.ISBN)

class Review(db.Model):

    ISBN = db.Column(db.String(13), db.ForeignKey('book.ISBN'), primary_key=True)
    username = db.Column(db.String(), db.ForeignKey('customer.username'), primary_key=True)
    score = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(), nullable=True)
    date = db.Column(db.Date(), nullable=False)

    def __init__(self, **kwargs):
        self.ISBN = kwargs['ISBN']
        self.username = kwargs['username']
        self.score = kwargs['score']
        self.description = kwargs['description']
        self.date = kwargs['date']

    def __repr__(self):
        return 'Review on {} by {}'.format(self.ISBN, self.username)

    __tablename__ = 'review'
    __tableargs__ = (
        CheckConstraint('score<=10 AND score>=0', name='score_between_0_and_10'),
    )

class Order(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date(), nullable=False)
    status = db.Column(db.Enum('in_progress', 'pending', 'shipped', name='order_statuses'), nullable=False)
    customer_username = db.Column(db.String(), db.ForeignKey('customer.username'))

    def __init__(self, **kwargs):
        self.date = kwargs['date']
        self.status = kwargs['status']
        self.customer_username = kwargs['customer_username']

    def __repr__(self):
        return 'Order {} by Customer {}'.format(self.id, self.customer_username)

    def total_price(self):
        return sum([books_orders.quantity * books_orders.book.price for books_orders in self.books_orders])

    def formatted_status(self):
        return humanize(self.status)

class BooksOrders(db.Model):

    order_id = db.Column(db.Integer(), db.ForeignKey('order.id'), primary_key=True)
    book_isbn = db.Column(db.String(13), db.ForeignKey('book.ISBN'), primary_key=True)
    quantity = db.Column(db.Integer(), nullable=False, default=1)
    order = db.relationship('Order',
                            backref=db.backref('books_orders', lazy='dynamic', cascade='all, delete-orphan'),
                            lazy='joined')
    book = db.relationship('Book')

    def __init__(self, **kwargs):
        self.quantity = kwargs['quantity']

    def total_price(self):
        return self.quantity * self.book.price
