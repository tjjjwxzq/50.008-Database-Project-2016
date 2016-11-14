import time
from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import login_required, current_user
from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import ARRAY
from app import db
from app.models import Book, Review, Order, BooksOrders, Feedback
from app.helpers import save
from app.forms import FilterBooksForm, CreateReviewForm, AddBookToOrderForm, CreateFeedbackForm

mod = Blueprint('my', __name__, url_prefix='/my')

@mod.route('/books/', methods=['GET', 'POST'])
@login_required
def book_index():
    filter_form = FilterBooksForm()

    if filter_form.validate_on_submit():
        search_dict = {k:v for k, v in filter_form.data.items() if v}
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

    add_book_to_order_forms = [AddBookToOrderForm() for i in range(len(books))]
    order_in_progress = current_user.order_in_progress()

    return render_template('my/book/index.html', books=books, filter_form=filter_form, add_book_to_order_forms=add_book_to_order_forms, order_in_progress=order_in_progress)

@mod.route('/books/<ISBN>')
@login_required
def show_book(ISBN):
    book = Book.query.get(ISBN)
    form = CreateFeedbackForm()
    return render_template('my/book/show.html', book=book, form=form)

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

@mod.route('/orders/')
@login_required
def order_index():
    orders = Order.query.all()

    return render_template('my/order/index.html', orders=orders)

@mod.route('/orders/', methods=['POST'])
@login_required
def create_order():
    order_params = {
        'date' : time.strftime('%Y-%m-%d%'),
        'status': 'in_progress',
        'customer_username': current_user.get_id()
    }
    order = Order(**order_params)

    if save(order):
        flash('You just started a new order! You can choose the books to add to your order below')
    else:
        flash('Failed to create order')

    return redirect(url_for('my.book_index'))

@mod.route('/orders/<order_id>', methods=['POST'])
@login_required
def update_order(order_id):
    # Check add book to order form validity
    form = AddBookToOrderForm(formdata=request.form)
    isbn = form.data['isbn']
    book = Book.query.get(isbn)

    if form.validate_on_submit():
        quantity = form.data['quantity']

        order = Order.query.get(order_id)
        books_orders = order.books_orders.filter_by(book=book).first()

        if not books_orders:
            books_orders = BooksOrders(quantity=quantity)
            books_orders.book = book
            order.books_orders.append(books_orders)
        else:
            books_orders.quantity = quantity

        if save(order):
            flash('Successfully updated number of copies of {} in your current order to {}!'.format(book.title, quantity))

            return redirect(url_for('my.book_index'))
        else:
            flash('Failed to add {} to your current order. Please try again'.format(book.title))

    # Render index template if add book to order form was invalid
    filter_form = FilterBooksForm()

    if filter_form.validate_on_submit():
        search_dict = {k:v for k, v in filter_form.data.items() if v}
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

    invalid_form_index = books.index(book)
    add_book_to_order_forms = [AddBookToOrderForm() for i in range(len(books))]
    add_book_to_order_forms[invalid_form_index] = form

    order_in_progress = current_user.order_in_progress()

    return render_template('my/book/index.html', books=books, filter_form=filter_form, add_book_to_order_forms=add_book_to_order_forms, order_in_progress=order_in_progress)

@mod.route('/orders/<order_id>')
@login_required
def show_order(order_id):
    order = Order.query.get(order_id)

    return render_template('my/order/show.html', order=order)

@mod.route('/order/')
@login_required
def current_order():
    order = current_user.order_in_progress()

    if order:
        return render_template('my/order/show.html', order=order)
    else:
        flash('You do not have an order in progress. You can start a new order here.')

        return redirect(url_for('my.book_index'))

@mod.route('/order/', methods=['POST'])
@login_required
def submit_order():
    order = current_user.order_in_progress()

    if order:
        order.status = 'pending'
        order.date = time.strftime('%Y-%m-%d')

        if save(order):
            flash('Order was successfully submitted!')

            return redirect(url_for('my.show_order', order_id=order.id))

    flash('Something went wrong when submitting your order. Please try again.')

    return redirect(url_for('my.current_order'))

@mod.route('/books/<ISBN>/<user>', methods=['GET', 'POST'])
@login_required
def create_feedback(ISBN,user):
    form = CreateFeedbackForm()

    book = Book.query.get(ISBN)

    review = Review.query.filter_by(username=user, ISBN=ISBN).first()

    if form.validate_on_submit():
        print(form.rating.data)
        feedback_params = {
            'customer_feedback': current_user.get_id(),
            'rating': form.rating.data,
            'customer_review': review.username,
            'ISBN': ISBN
        }
        if Feedback.query.filter_by(customer_feedback=current_user.get_id(), ISBN=book.ISBN).first() is None:
            if (current_user.get_id()!=review.username):
                feedback = Feedback(**feedback_params)

                if save(feedback):
                    flash("Feedback created successfully!")

                    return redirect(url_for('my.show_book', ISBN=book.ISBN))
                else:
                    flash("Failed to create review. Please try again")
            else:
                flash("You may not create feedback for your own review")
        else:
            flash("You have already entered a feedback.")


    return render_template('my/book/show.html', book=book, review=review, form=form)
