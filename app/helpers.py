from app import db

def save(resource):
    db.session.add(resource)

    try:
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        db.session.flush()
        return False
