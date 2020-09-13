from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, current_user
from flask_sqlalchemy import event
from . import db, login_manager, bcrypt

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')
    def is_accessible(self):
       if current_user.is_authenticated:
           return current_user.permission.lower() == 'admin'

class Title(db.Model):
    __tablename__ = 'Titles'
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(100), nullable=False)
    subheading = db.Column(db.String(100))
    href = db.Column(db.String(100), default='#')

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), default='None')
    lastname = db.Column(db.String(20), default='None')
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    permission = db.Column(db.String(100), default='Basic')

    def is_accessible(self):
       if current_user.is_authenticated:
           return current_user.permission == 'Admin'

class MyModelView(ModelView):
    column_exclude_list = ('password'),
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.permission == 'Admin'

# Listens for row creation in Flask-Admin
@event.listens_for(User.password, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        # DECODE password. Postegresql will hash it again
        return bcrypt.generate_password_hash(value).decode('UTF-8')
    return value