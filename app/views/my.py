import time
from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import ARRAY
from app import db
from app.models import Customer, Book, Review
from app.helpers import save
from app.forms import FilterBooksForm, CreateReviewForm

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

@mod.route('/books/<ISBN>/reviews', methods=['GET', 'POST'])
@login_required
def create_book_review(ISBN):
    form = CreateReviewForm()
    book = Book.query.get(ISBN)

    if form.validate_on_submit():
        review_params = {
            'ISBN': book.ISBN,
            'username': current_user.get_id(),
            'score': form.score.data,
            'description': form.description.data,
            'date': time.strftime("%x")
        }

        if Review.query.filter_by(username=current_user.get_id(), ISBN=book.ISBN).first() is None:
            review = Review(**review_params)

            if save(review):
                flash("Review created successfully!")

                return redirect(url_for('my.show_book', ISBN=book.ISBN))
            else:
                flash("Failed to create review. Please try again.")
        else:
            flash("You have already entered a review for this book.")

    return render_template('my/book/new.html', book=book, form=form)
