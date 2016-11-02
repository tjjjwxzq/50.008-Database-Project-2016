from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from app import login_manager
from app.forms import CustomerSignUpForm, CustomerLoginForm
from app.models import Customer
from app.helpers import save

mod = Blueprint('customer', __name__, url_prefix='/customer')

login_manager.login_view = "customer.login"

@login_manager.user_loader
def load_customer(customer_username):
    return Customer.query.get(customer_username)

@mod.route('/login', methods=['GET', 'POST'])
def login():
    # Handle form POST request
    form = CustomerLoginForm()

    if form.validate_on_submit():
        customer = Customer.query.get(form.username.data)

        if customer.verify_password(form.password.data) and login_user(customer):
            flash('Logged in successfully!')

            return redirect(url_for('pages.index'))

        else:
            flash('Failed to log in. Username or password was incorrect.')

    return render_template('customer/login.html', form=form)

@mod.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!')
    return redirect(url_for('customer.login'))

@mod.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = CustomerSignUpForm()

    if form.validate_on_submit():
        customer_params = form.data.copy()
        del customer_params['password_confirmation']
        new_customer = Customer(**customer_params)

        if save(new_customer):
            login_user(new_customer)
            flash('Your account was successfully created! Welcome to DBookstore!')

            return redirect(url_for('pages.index'))
        else:
            flash('Account creation was unsuccessful. Please try again.')

    return render_template('customer/sign_up.html', form=form)
