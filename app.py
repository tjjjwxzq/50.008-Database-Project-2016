import os
from functools import wraps
import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app, session_options={'autoflush': False})
login_manager = LoginManager()
login_manager.init_app(app)

from models import Customer
from forms import CustomerLoginForm, CustomerSignUpForm

# HELPERS
def save(resource):
    db.session.add(resource)

    try:
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        db.session.flush()
        return False

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
    form = CustomerSignUpForm()

    if form.validate_on_submit():
        customer_params = form.data.copy()
        del customer_params['password_confirmation']
        new_customer = Customer(**customer_params)

        if save(new_customer):
            login_user(new_customer)
            flask.flash('Your account was successfully created! Welcome to DBookstore!')

            return flask.redirect(flask.url_for('index'))
        else:
            flask.flash('Account creation was unsuccessful. Please try again.')

    return flask.render_template('customer/sign_up.html', form=form)

# Customer Login
@app.route('/customer/login', methods=['GET', 'POST'])
def customer_login():
    # Handle form POST request
    form = CustomerLoginForm()

    if form.validate_on_submit():
        customer = Customer.query.get(form.username.data)

        if customer.verify_password(form.password.data) and login_user(customer):
            flask.flash('Logged in successfully!')

            return flask.redirect(flask.url_for('index'))

        else:
            flask.flash('Failed to log in. Username or password was incorrect.')

    return flask.render_template('customer/login.html', form=form)

# Customer Logout
@app.route('/customer/logout')
@login_required
def customer_logout():
    logout_user()
    flask.flash('Logged out successfully!')
    return flask.redirect(flask.url_for('customer_login'))
