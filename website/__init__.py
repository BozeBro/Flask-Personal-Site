from flask import Flask
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .configfile import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
app.config.from_object(ProductionConfig())

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from . import routes
from .models import Title, User, MyAdminIndexView, MyModelView

admin = Admin(app, index_view=MyAdminIndexView())
#All Models are in .models
admin.add_views(ModelView(Title, db.session), ModelView(User, db.session))