def create_app():
    from flask import Flask
    from flask_admin import Admin, AdminIndexView
    from flask_admin.contrib.sqla import ModelView
    from .configfile import DevelopmentConfig
    from .models import bcrypt, db, login_manager, admin
    from . import routes
    from .models import Title, User, MyAdminIndexView, MyModelView
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    admin.init_app(app, index_view=MyAdminIndexView)
    admin.add_views(MyModelView(Title, db.session), MyModelView(User, db.session))
    return app
