import os
from flask import Flask
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = os.environ['PERSONAL_SECRET']

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from . import routes
from .models import Title, User, MyAdminIndexView, MyModelView

admin = Admin(app, index_view=MyAdminIndexView())
#All Models are in .models
admin.add_views(MyModelView(Title, db.session), MyModelView(User, db.session))