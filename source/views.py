from flask import Blueprint, render_template, redirect, url_for
from instance.db import load, loadunique
from flask_login import login_required, logout_user, current_user
from .models import User

views = Blueprint('views', __name__)

#--- PAGES ---
# 0. LOGIN PAGE
@views.route('/login')
def login():
  return render_template('login.html',
                         base=load('base', '*'),
                         services=load('services', '*'),
                         departments=loadunique('users', 'udepartment'),
                         positions=loadunique('users', 'uposition'),
                         supervisors=loadunique('users', 'usupervisor'),
                         cur_username = loadunique('base', 'bdata')[4][0])

# 1. MAIN PAGE
@views.route('/',  methods=['GET', 'POST'])
@login_required
def mainpage():
  return render_template('mainpage.html',
                          base = load('base', '*'),
                          services = load('services', '*'),
                          cur_username = current_user.ufname + ' ' + current_user.ulname)


