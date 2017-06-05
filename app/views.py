# coding: utf-8
from app import app
from flask import render_template, redirect, url_for, request
import flask_login
import os

# Our mock database.
users = {'davian': {'pw': 'visualking!'}}

app.secret_key = 'davian-3nff3infalfifh8serfh94fnkdn'  # Change this!

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	if request.method == 'GET':
		return render_template("login.html")

	user_id = request.form['user_id']
	if request.form['pw'] == users[user_id]['pw']:
		user = User()
		user.id = user_id
		flask_login.login_user(user)
		return redirect(url_for('protected'))

	return 'Bad login'

@app.route('/admin_title')
@flask_login.login_required
def admin_title():
	print('call admin_title()')
	return render_template("admin_title.html")

@app.route('/admin_about')
@flask_login.login_required
def admin_about():
	print('call admin_about()')
	return render_template("admin_about.html")

@app.route('/admin_news')
@flask_login.login_required
def admin_news():
	print('call admin_news()')
	return render_template("admin_news.html")

@app.route('/admin_research')
@flask_login.login_required
def admin_research():
	print('call admin_research()')
	return render_template("admin_research.html")

@app.route('/admin_member')
@flask_login.login_required
def admin_member():
	print('call admin_member()')
	return render_template("admin_member.html")

@app.route('/admin_teaching')
@flask_login.login_required
def admin_teaching():
	print('call admin_teaching()')
	return render_template("admin_teaching.html")

@app.route('/admin_publication')
@flask_login.login_required
def admin_publication():
	print('call admin_publication()')
	return render_template("admin_publication.html")

@app.route('/protected')
@flask_login.login_required
def protected():
    # return 'Logged in as: ' + flask_login.current_user.id
    return render_template("admin_title.html")

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.user_loader
def user_loader(user_id):
    if user_id not in users:
        return

    user = User()
    user.id = user_id
    return user


@login_manager.request_loader
def request_loader(request):
    user_id = request.form.get('user_id')
    if user_id not in users:
        return

    user = User()
    user.id = user_id

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['pw'] == users[user_id]['pw']

    return user

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'