from sqlalchemy import text

customer = text(
    """INSERT INTO customer VALUES
    ('user1', 'password', 'foo', 'bar', '12345678', '8 Somapah Rd')"""
)
