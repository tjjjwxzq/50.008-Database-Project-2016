from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_required
from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import ARRAY
from app import db
from app.models import Customer, Book
from app.helpers import save
from app.forms import FilterBooksForm

mod = Blueprint('my', __name__, url_prefix='/my')

@mod.route('/books/', methods=['GET', 'POST'])
@login_required
def book_index():
    form = FilterBooksForm()

    if form.validate_on_submit():
        search_dict = {k:v for k, v in form.data.items() if v}
        books = Book.query
        for k, v in search_dict.items():
            if k == 'authors':
                authors = [author.strip() for author in v.split(', ')]
                books = books.filter(cast(getattr(Book, k), ARRAY(db.Text())).contains(authors))
            else:
                books = books.filter(getattr(Book, k).ilike('%{}%'.format(v)))
        books = books.all()
    else:
        books = Book.query.all()

    return render_template('my/book/index.html', books=books, form=form)

@mod.route('/books/<ISBN>')
@login_required
def show_book(ISBN):
    book = Book.query.get(ISBN)
    return render_template('my/book/show.html', book=book)
