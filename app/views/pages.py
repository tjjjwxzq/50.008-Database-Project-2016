from flask import Blueprint, render_template

mod = Blueprint('pages', __name__)

@mod.route('/')
def index():
    return render_template('index.html')
