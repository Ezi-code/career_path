from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# CONFIGURATIONS

# app configuration
app = Flask(__name__,"/static")
# database configuration 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
# secrete key for secure submission of forms 
app.config['SECRET_KEY'] = "os.getenv('SECRET_KEY')"
# database instantiation 
db = SQLAlchemy(app)
# Password encryptor instantiation
bcrypt = Bcrypt(app)
# Login manager configuration 
login_manager = LoginManager(app)
# login page 
login_manager.login_view = "admin_login"
# Alert type 
login_manager.login_message_category = 'info'


from . import routes

