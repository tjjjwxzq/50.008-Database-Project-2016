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

def run():
    db.engine.execute(insert_customer)
    db.engine.execute(insert_store_manager)

def clear():
    db.engine.execute(delete_customer)
    db.engine.execute(delete_store_manager)
