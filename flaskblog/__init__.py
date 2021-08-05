from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager


app = Flask(__name__)
app.config['SECRET_KEY'] = '60af430d62080dc3a656ed7b0b1ff46efc8b2ebb98fcaaae93510e52b98c1dcf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from flaskblog import routes