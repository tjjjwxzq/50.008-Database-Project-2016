import os
from functools import wraps
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app, session_options={'autoflush': False})
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)

from app.views import pages
from app.views import customer
from app.views import store_manager

app.register_blueprint(pages.mod)
app.register_blueprint(customer.mod)
app.register_blueprint(store_manager.mod)
