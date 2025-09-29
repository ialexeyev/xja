from flask import Blueprint 
from . import userDB
from flask_login import UserMixin


models = Blueprint('models', __name__)

#--- DATABASE MODELS ---
# 1. USERS DATABASE MODEL --
class User(userDB.Model, UserMixin):
  id = userDB.Column(userDB.Integer, primary_key=True)
  uid = userDB.Column(userDB.String(30), unique=True)
  ufname = userDB.Column(userDB.String(25))
  ulname = userDB.Column(userDB.String(30))
  umail = userDB.Column(userDB.String(40), unique=True)
  udepartment = userDB.Column(userDB.String(40))
  usupervisor = userDB.Column(userDB.String(40))
  uposition = userDB.Column(userDB.String(40))
  uaccess = userDB.Column(userDB.String(15))
  upass = userDB.Column(userDB.String(20))

