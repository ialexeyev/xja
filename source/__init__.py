from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

userDB = SQLAlchemy()
USERDB_NAME = "users.db"

def create_app():
  app = Flask(__name__, static_folder='static', static_url_path='/static')
  app.config['SECRET_KEY'] = 'prismgt40xja'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{USERDB_NAME}'
  userDB.init_app(app)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

  from .models import User
  
  with app.app_context():
    userDB.create_all()

  login_manager = LoginManager()
  login_manager.login_view = 'views.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
      return User.query.get(int(id))


  return app


def create_database(app):
  if not path.exists('instance/' + USERDB_NAME):
      userDB.create_all(app=app)
      print('Created Database!')