import os
from functools import wraps
import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app, session_options={'autoflush': False})
login_manager = LoginManager()
login_manager.init_app(app)

from models import Customer
from forms import CustomerLoginForm

# LOGIN HELPERS
@login_manager.user_loader
def load_customer(customer_username):
    return Customer.query.get(customer_username)

# VIEWS

# Home page
@app.route('/')
def index():
    return flask.render_template('index.html')

# Customer Registration
@app.route('/customer/sign_up', methods=['GET', 'POST'])
def customer_sign_up():
    form = CustomerSignupForm()

    if form.validate_on_submit():
        pass

# Customer Login
@app.route('/customer/login', methods=['GET', 'POST'])
def customer_login():
    form = CustomerLoginForm()

    if form.validate_on_submit():
        customer = Customer.query.get(form.username.data)

        if customer and customer.verify_password(form.password.data) and login_user(customer):
            flask.flash('Logged in successfully!')

            return flask.redirect(flask.url_for('index'))

    return flask.render_template('login.html', form=form)
