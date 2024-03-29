import time
from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import login_required, current_user
from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import ARRAY
from app import db
from app.models import Book, Review, Order, BooksOrders, Feedback, Customer
from app.helpers import save
from app.forms import FilterBooksForm, CreateReviewForm, AddBookToOrderForm, CreateFeedbackForm, SetNofTopReviewsForm

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

    # Book recommendation
    ordered_book_isbn = request.args.get('ordered_book_isbn')
    if ordered_book_isbn:
        ordered_book = Book.query.get(ordered_book_isbn)

        if ordered_book:
            customers_who_ordered_book = [customer for customer in ordered_book.customers() if customer.username != current_user.get_id()]

            recommended_books = []
            for customer in customers_who_ordered_book:
                for customer_order in customer.orders.all():
                    for books_orders in customer_order.books_orders.all():
                        if books_orders.book != ordered_book:
                            recommended_books.append(books_orders.book)

            recommended_books = sorted(set(recommended_books), key=lambda book: book.total_sales_to_similar_customers(ordered_book))
        else:
            recommended_books = []
    else:
        ordered_book = None
        recommended_books = []

    recommended_books_order_forms = [AddBookToOrderForm() for i in range(len(recommended_books))]

    return render_template('my/book/index.html',
                           books=books,
                           filter_form=filter_form,
                           add_book_to_order_forms=add_book_to_order_forms,
                           order_in_progress=order_in_progress,
                           recommended_books=recommended_books,
                           recommended_books_order_forms=recommended_books_order_forms,
                           ordered_book=ordered_book)

@mod.route('/books/<ISBN>', methods=['GET', 'POST'])
@login_required
def show_book(ISBN):
    book = Book.query.get(ISBN)
    feedback_form = CreateFeedbackForm()
    top_review_form = SetNofTopReviewsForm()
    current_user_review = current_user.reviews.filter_by(ISBN=ISBN).first()
    reviews_queried = Review.query.filter_by(ISBN=ISBN)

    if top_review_form.validate_on_submit():
        n = top_review_form.num_of_reviews.data
        if n > 0:
            whole_reviews = []
            for review in reviews_queried:
                avg_of_feedbacks = get_average_feedback(review)
                whole_reviews.append((review, avg_of_feedbacks, feedback_exists(review)))

            sorted_reviews = sorted(whole_reviews, key=lambda x:x[1], reverse=True)
            top_n_reviews = sorted_reviews[0:n]
            reviews = top_n_reviews

    else:
        reviews = []
        for r in reviews_queried:
            reviews.append((r, get_average_feedback(r), feedback_exists(r)))

    return render_template('my/book/show.html', book=book, feedback_form=feedback_form, top_review_form=top_review_form, current_user_review=current_user_review, reviews=reviews, user=current_user.get_id())

def get_average_feedback(review):
    feedbackList = review.feedbacks
    temp = []
    for f in feedbackList:
        temp.append(f.rating)
    if len(temp) == 0:
        mean = -1 #Means no feedback given
    else:
        mean = float(sum(temp)) / float(len(temp))

    return mean

def feedback_exists(review):
    feedbackList = review.feedbacks
    for f in feedbackList:
        if f.customer_feedback == current_user.get_id():
            return True
    return False

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
            'date': time.strftime("%Y-%m-%d")
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

    return render_template('my/book/review/new.html', book=book, form=form)

@mod.route('/orders/')
@login_required
def order_index():
    orders = current_user.orders.all()

    return render_template('my/order/index.html', orders=orders)

@mod.route('/orders/', methods=['POST'])
@login_required
def create_order():
    order_params = {
        'date' : time.strftime('%Y-%m-%d'),
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

            return redirect(url_for('my.book_index', ordered_book_isbn=book.ISBN))
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

@mod.route('/books/<ISBN>/<user>', methods=['POST'])
@login_required
def create_feedback(ISBN, user):
    feedback_form = CreateFeedbackForm()
    top_review_form = SetNofTopReviewsForm()
    book = Book.query.get(ISBN)
    review = Review.query.filter_by(username=user, ISBN=ISBN).first()

    if feedback_form.validate_on_submit():
        feedback_params = {
            'customer_feedback': current_user.get_id(),
            'rating': feedback_form.rating.data,
            'customer_review': review.username,
            'ISBN': ISBN
        }
        if Feedback.query.filter_by(customer_feedback=current_user.get_id(), ISBN=book.ISBN, customer_review=user).first() is None:
            if current_user.get_id() != review.username:
                feedback = Feedback(**feedback_params)

                if save(feedback):
                    flash("Feedback created successfully!")

                    return redirect(url_for('my.show_book', ISBN=book.ISBN))
                else:
                    flash("Failed to create feedback. Please try again")
            else:
                flash("You may not create feedback for your own review")
        else:
            flash("You have already entered a feedback.")

    return render_template('my/book/show.html', book=book, review=review, feedback_form=feedback_form, top_review_form=top_review_form)

@mod.route('/account')
@login_required
def get_account_information():
    user = Customer.query.get(current_user.get_id())

    return render_template('my/user/account.html', user=user)

@mod.route('/reviews')
@login_required
def get_review_history():
    user = Customer.query.get(current_user.get_id())
    reviews = []
    for r in user.reviews:
        reviews.append((r, get_average_feedback(r)))

    return render_template('my/user/reviews.html', user=user, reviews=reviews)

@mod.route('/feedback')
@login_required
def get_feedback_history():
    user = Customer.query.get(current_user.get_id())

    return render_template('my/user/feedback.html', user=user)
