from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app import login_manager
from app.forms import StoreManagerLoginForm
from app.models import StoreManager

mod = Blueprint('store_manager', __name__, url_prefix='/store_manager')

@login_manager.user_loader
def load_store_manager(store_manager_username):
    return StoreManager.query.get(store_manager_username)

@mod.route('/login', methods=['GET', 'POST'])
def login():
    # Handle form POST request
    form = StoreManagerLoginForm()

    if form.validate_on_submit():
        store_manager = StoreManager.query.get(form.username.data)

        if store_manager.verify_password(form.password.data) and login_user(store_manager):
            flash('Logged in successfullY!')

            return redirect(url_for('pages.index'))
        else:
            flash('Failed to log in. Username or password was incorrect.')

    return render_template('store_manager/login.html', form=form)
