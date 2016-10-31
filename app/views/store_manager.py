from functools import wraps
from flask import Blueprint, render_template, redirect, flash, url_for, session
from app import app
from app.forms import StoreManagerLoginForm
from app.models import StoreManager

mod = Blueprint('store_manager', __name__, url_prefix='/store_manager')

# Login helpers, because FLask Login doesn't support multiple user models

def store_manager_logged_in():
    return session.get('store_manager', None) != None

app.jinja_env.globals.update(store_manager_logged_in=store_manager_logged_in)

def load_store_manager(store_manager_username):
    return StoreManager.query.get(store_manager_username)

def login_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        username = session.get('store_manager')
        if username:
            store_manager = load_store_manager(username)
            if store_manager:
                return function(*args, **kwargs)
            else:
                flash('Store manager no longer exists')
                return redirect(url_for('store_manager.login'))
        else:
            flash('Please log in to access this page')
            return redirect(url_for('store_manager.login'))
    return wrapper

@mod.route('/login', methods=['GET', 'POST'])
def login():
    # Handle form POST request
    form = StoreManagerLoginForm()

    if form.validate_on_submit():
        store_manager = StoreManager.query.get(form.username.data)

        if store_manager.verify_password(form.password.data):
            session['store_manager'] = store_manager.username
            flash('Logged in successfully!')
            print(session)

            return redirect(url_for('pages.index'))
        else:
            flash('Failed to log in. Username or password was incorrect.')

    return render_template('store_manager/login.html', form=form)

@mod.route('/logout')
@login_required
def logout():
    session.pop('store_manager', None)
    flash('Logged out successfully!')
    return redirect(url_for('store_manager.login'))
