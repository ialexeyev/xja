from flask import Blueprint, request
from .models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)


#--- PROCESSORS ---
# 1. Sign in process
@auth.route('/loginprocess', methods=['POST'])
def loginprocess():
  result = "checking"
  if request.method == 'POST':
    userID = request.form['userid']
    userPASS = request.form['userpass']

    user = User.query.filter_by(uid=userID).first()
    if user:
      if check_password_hash(user.upass, userPASS):
        login_user(user, remember=True)
        result = "OK"
      else:
        result = "PASS NOK"
    else:
      result = "ID NOK"
  return result


# 2. Sign up process
@auth.route('/signupprocess', methods=['POST'])
def signupprocess():
  if (newuser(request.form['newfname'], request.form['newlname'],
              request.form['newmail'], request.form['newdep'],
              request.form['newpos'], request.form['newsup']) == "OK"):
    return "OK"
  else:
    return "NOK"


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
  logout_user()
  return 'OK'
