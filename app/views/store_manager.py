import datetime
from functools import wraps
from flask import Blueprint, render_template, redirect, flash, url_for, session
from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import ARRAY
from app import app, db
from app.forms import StoreManagerLoginForm, NewBookForm, EditBookForm, StatisticsForm
from app.models import StoreManager, Book
from app.helpers import save

mod = Blueprint('store_manager', __name__, url_prefix='/store_manager')

# Statistics helpers

def get_publishers():
    return {book.publisher for book in Book.query.all()}

def get_authors():
    nested_authors = [book.authors for book in Book.query.all()]
    return {author for authors in nested_authors for author in authors}

def publisher_sales_in_month(publisher, month, year):
    books = Book.query.filter_by(publisher=publisher)
    return sum([book.total_sales_in_month(month, year) for book in books])

def author_sales_in_month(author, month, year):
    books = Book.query.filter(cast(Book.authors, ARRAY(db.Text())).contains([author]))
    return sum([book.total_sales_in_month(month, year) for book in books])

def most_popular_publishers_in_month(m, month, year):
    publishers = [publisher for publisher in get_publishers() if publisher_sales_in_month(publisher, month, year) > 0]
    return sorted(publishers, key=lambda publisher: publisher_sales_in_month(publisher, month, year), reverse=True)[0:m]

def most_popular_authors_in_month(m, month, year):
    authors = [author for author in get_authors() if author_sales_in_month(author, month, year) > 0]
    return sorted(authors, key=lambda author: author_sales_in_month(author, month, year), reverse=True)[0:m]

def most_popular_books_in_month(m, month, year):
    books = [book for book in Book.query.all() if book.total_sales_in_month(month, year) > 0]
    return sorted(books, key=lambda book: book.total_sales_in_month(month, year), reverse=True)[0:m]
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

@mod.route('/books')
@login_required
def book_index():
    books = Book.query.all()
    return render_template('store_manager/book/index.html', books=books)

@mod.route('/books/new', methods=['GET', 'POST'])
@login_required
def new_book():
    # Handle form POST request
    form = NewBookForm()

    if form.validate_on_submit():
        book_params = form.data.copy()
        book_params['authors'] = [author.strip() for author in book_params['authors'].split(',')]
        book_params['keywords'] = [keyword.strip() for keyword in book_params['keywords'].split(',')]

        book = Book(**book_params)

        if save(book):
            flash('New book created successfully!')

            return redirect(url_for('store_manager.edit_book', ISBN=book.ISBN))
        else:
            flash('Failed to create new book. Please try again.')

    return render_template('store_manager/book/new.html', form=form)

@mod.route('/books/<ISBN>/edit', methods=['GET', 'POST'])
@login_required
def edit_book(ISBN):
    # Handle form PUT request
    book = Book.query.get(ISBN)
    form = EditBookForm(obj=book)

    if form.validate_on_submit():
        authors = [author.strip() for author in form.data['authors'].split(',')]
        keywords = [keyword.strip() for keyword in form.data['keywords'].split(',')]

        form.populate_obj(book)
        book.authors = authors
        book.keywords = keywords

        if save(book):
            flash('Book details updated successfully!')

        else:
            flash('Failed to update book details. Please try again.')

    return render_template('store_manager/book/edit.html', form=form, book=book)

@mod.route('/statistics', methods=['GET', 'POST'])
@login_required
def statistics():
    form = StatisticsForm()

    if form.validate_on_submit():
        month = form.data['month']
        number = form.data['number']
    else:
        month = datetime.date.today().month
        number = 10

    year = datetime.date.today().year
    books = most_popular_books_in_month(number, month, year)
    authors = most_popular_authors_in_month(number, month, year)
    publishers = most_popular_publishers_in_month(number, month, year)

    return render_template('store_manager/statistics/show.html', form=form, books=books, authors=authors, publishers=publishers)
