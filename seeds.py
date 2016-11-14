from app import db
from sqlalchemy import text

insert_customer = text(
    """INSERT INTO customer VALUES
    ('user1', 'password', 'foo', 'bar', '12345678', '8 Somapah Rd')"""
)

delete_customer = text(
    'DELETE FROM customer'
)

insert_store_manager = text(
    """INSERT INTO store_manager VALUES
    ('store_manager1', 'password')"""
)

delete_store_manager = text(
    'DELETE FROM store_manager'
)

insert_books = text(
    """INSERT INTO book ("ISBN", title, authors, publisher, year_of_publication, stock, price, format, subject, keywords) VALUES
    ('9780321197849', 'An Introduction to Database Systems', '{"C.J. Date"}', 'Pearson', 2003, 5, 206.42, 'hardcover', 'Database', '{"database", "computer science"}'),
    ('9781783555130', 'Python Machine Learning', '{Sebastian Raschka}', 'Packt Publishing', 2015, 10, 40.49, 'softcover', 'Machine Learning', '{"machine learning", "data science", "computer science", "statistical learning"}'),
    ('9781461471370', 'An Introduction to Statistical Learning: with Applications in R', '{"Gareth James", "Daniela Witten", "Trevor Hastie", "Robert Tibshirani"}', 'Springer', 2013, 2, 72.62, 'hardcover', 'Statistical Learning', '{"machine learning", "data science", "computer science", "statistical learning"}')"""
)

delete_books = text(
    'DELETE FROM book'
)

insert_reviews = text(
    """INSERT INTO review ("ISBN", username, score, description, date) VALUES
    ('9780321197849', 'user1', 9, 'Very Informative like MeiHui', CURRENT_DATE)"""
)

delete_reviews = text(
    'DELETE FROM review'
)

delete_orders = text(
    'DELETE FROM "order"'
)

def run():
    db.engine.execute(insert_customer)
    db.engine.execute(insert_store_manager)
    db.engine.execute(insert_books)
    db.engine.execute(insert_reviews)

def clear():
    db.engine.execute(delete_orders)
    db.engine.execute(delete_customer)
    db.engine.execute(delete_store_manager)
    db.engine.execute(delete_books)
    db.engine.execute(delete_reviews)

