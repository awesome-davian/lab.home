# coding: utf-8
from app import app
# from .manager import login_manager
from flask import render_template, redirect, url_for, request, flash, g, jsonify
import os
# from .forms import LoginForm
# from .models import User


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/admin', methods=['GET'])
def login():
	print("step-1")
	print(request)
	email = request.form['email']
	password = request.form['password']
	print("step-2")
	if User(user_name, password).login() is False :
		return render_template('login.html', login_fail=1)
	session_key = redis_session().save_session(user_name)

	session['session_key'] = session_key
	print("step-3")
	return redirect(url_for('admin'))

	# form = LoginForm()
	# if request.method == 'POST' and form.validate_on_submit():
	# 	user = app.config['USERS_COLLECTION'].find_one({"_id": form.email.data})
	# 	if user and User.validate_login(user['password'], form.password.data):
	# 		user_obj = User(user['_id'])
	# 		login_user(user_obj)
	# 		flash("Logged in successfully!", category='success')
	# 		return redirect(request.args.get("next") or url_for("write"))
	# 	flash("Wrong username or password!", category='error')
	# return render_template('login.html', title='login', form=form)

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

# @login_manager.user_loader
# def load_user(email):
# 	u = app.config['USERS_COLLECTION'].find_one({"_id": email})
# 	if not u:
# 		return None
# 	return User(u['_id'])
