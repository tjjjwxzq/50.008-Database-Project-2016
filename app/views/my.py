from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_required
from app.models import Customer, Book
from app.helpers import save

mod = Blueprint('my', __name__, url_prefix='/my')

@mod.route('/books')
@login_required
def book_index():
    books = Book.query.all()
    return render_template('my/book/index.html', books=books)

@mod.route('/books/<ISBN>')
@login_required
def show_book(ISBN):
    pass
