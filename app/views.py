# coding: utf-8
from app import app
from flask import render_template, redirect, url_for, request
import flask_login
import os
from app import db, models, db_wrapper
from sqlalchemy import desc


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
		return redirect(url_for('admin_title'))

	return flask.abort(400)

@app.route('/admin_title')
@flask_login.login_required
def admin_title():
	
	labinfo = models.LabInfo.query.filter_by(id = 1).first()
	if labinfo == None:
		print('admin_title(), Could not found a Lab. information.')
		return redirect(url_for('protected'))
	
	return render_template("admin_title.html", description=labinfo.description, 
		sub_description=labinfo.sub_description, bg_path=labinfo.background_img_path)

@app.route('/admin_title_submit', methods=['GET','POST'])
@flask_login.login_required
def admin_title_submit():

	desc_text = request.form['description']
	subdesc_text = request.form['sub_description']
	background_image = request.files['bg_image']

	print('admin_title_submit(), description: %s, sub_description: %s' % (desc_text, subdesc_text))

	db_wrapper.update_lab_info(in_desc = desc_text, 
		in_sub_desc = subdesc_text, in_bg_image = background_image)

	return redirect(url_for('admin_title'))

@app.route('/admin_about')
@flask_login.login_required
def admin_about():
	
	about = models.About.query.filter_by(id = 1).first()

	if about != None:
		text = about.text
		sub_text = about.sub_text
	else:
		print('call admin_about(), Could not found a About. information.')
		text = ''
		sub_text = ''
		
	return render_template("admin_about.html", about_text=text, 
		about_sub_text=sub_text)

@app.route('/admin_about_submit', methods=['GET','POST'])
@flask_login.login_required
def admin_about_submit():
	
	text = request.form['about_text']
	sub_text = request.form['about_sub_text']

	print('admin_about_submit(), text: %s, sub_text: %s' % (text, sub_text))

	db_wrapper.update_about(in_text = text, in_sub_text = sub_text)

	return redirect(url_for('admin_about'))

@app.route('/admin_news/<int:page_num>')
@flask_login.login_required
def admin_news(page_num):

	print('admin_news(), page_num: %d' % (page_num))

	count_per_page = 10
	news_all = models.News.query.order_by(desc(models.News.date)).all()
	news_count = len(news_all)
	page_count = int((news_count-1) / count_per_page + 1)

	start_idx = (count_per_page * (page_num-1)) + 1
	end_idx = (count_per_page * (page_num-1)) + count_per_page
	if news_count < end_idx:
		end_idx = news_count

	news_page = []
	idx = 1
	for item in news_all:
		if start_idx <= idx and idx <= end_idx:
			news_page.append(item)
		idx += 1

	print('admin_news(), news_count: %d, page_count: %d' % (news_count, page_count))
	
	return render_template("admin_news.html", page_num = page_num, page_count = page_count, news_count = news_count, news_page = news_page, start_idx = start_idx, end_idx = end_idx)

@app.route('/admin_news/admin_news_create_new', methods=['GET', 'POST'])
@flask_login.login_required
def admin_news_create_new():
	
	news_title = request.form['news_title']
	news_contents = request.form['news_contents']
	news_date = request.form['news_date']

	print('admin_news_create_new(), news_title: %s, news_contents: %s, news_date: %s' % (news_title, news_contents, news_date))

	db_wrapper.insert_news(in_news_title=news_title, in_news_contents=news_contents, in_news_date=news_date)

	return redirect(url_for('admin_news', page_num=1))

@app.route('/admin_news/admin_news_edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_news_edit():

	print('admin_news_edit()')
	
	news_id = request.form['news_id']
	news_title = request.form['news_title']
	news_contents = request.form['news_contents']
	news_date = request.form['news_date']
	
	print('admin_news_edit(), news_title: %s, news_contents: %s, news_date: %s' % (news_title, news_contents, news_date))

	db_wrapper.update_news(in_news_id = news_id, in_news_title=news_title, in_news_contents=news_contents, in_news_date=news_date)

	return redirect(url_for('admin_news', page_num=1))

@app.route('/admin_news/admin_news_delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_news_delete():

	print('admin_news_delete()')
	
	news_id = request.form['news_id']
	
	print('admin_news_delete(), news_id: %s' % (news_id))

	db_wrapper.delete_news(in_news_id = news_id)

	return redirect(url_for('admin_news', page_num=1))

@app.route('/admin_research/<int:page_num>')
@flask_login.login_required
def admin_research(page_num):
	
	print('admin_research(), page_num: %d' % (page_num))

	count_per_page = 10
	research_all = models.Research.query.all()
	research_count = len(research_all)
	page_count = int((research_count-1) / count_per_page + 1)

	start_idx = (count_per_page * (page_num-1)) + 1
	end_idx = (count_per_page * (page_num-1)) + count_per_page
	if research_count < end_idx:
		end_idx = research_count

	research_page = []
	idx = 1
	for item in research_all:
		if start_idx <= idx and idx <= end_idx:
			research_page.append(item)
		idx += 1

	print('admin_research(), research_count: %d, page_count: %d' % (research_count, page_count))
	
	return render_template("admin_research.html", page_num = page_num, page_count = page_count, research_count = research_count, research_page = research_page, start_idx = start_idx, end_idx = end_idx)

@app.route('/admin_research/new', methods=['GET', 'POST'])
@flask_login.login_required
def admin_research_new():

	print('admin_research_create_new()')	

	title = request.form['title']
	text1 = request.form['text1']
	text2 = request.form['text2']
	teaser_image_path = request.form['teaser_image']
	member = request.form['member']
	publications = request.form['publications']
	is_activated = request.form['is_activated']

	print('admin_research_create_new(), title: %s, text1: %s, text2: %s' % (title, text1, text2))

	db_wrapper.insert_research(title=title, text1=text1, text2=text2, teaser_image_path=teaser_image_path, member=member, publications=publications, is_activated=is_activated)

	return redirect(url_for('admin_research', page_num=1))

@app.route('/admin_research/edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_research_edit():

	print('admin_research_edit()')
	
	research_id = request.form['research_id']
	title = request.form['title']
	text1 = request.form['text1']
	text2 = request.form['text2']
	teaser_image_path = request.form['teaser_image']
	member = request.form['member']
	publications = request.form['publications']
	is_activated = request.form['is_activated']
	
	print('admin_research_edit(), title: %s, text1: %s, text2: %s' % (title, text1, text2))

	db_wrapper.update_research(id=research_id, title=title, text1=text1, text2=text2, teaser_image_path=teaser_image_path, member=member, publications=publications, is_activated=is_activated)

	return redirect(url_for('admin_research', page_num=1))

@app.route('/admin_research/delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_research_delete():

	print('admin_research_delete()')
	
	research_id = request.form['research_id']
	
	print('admin_research_delete(), research_id: %s' % (research_id))

	db_wrapper.delete_research(id = research_id)

	return redirect(url_for('admin_research', page_num=1))

@app.route('/admin_member/<int:page_num>')
@flask_login.login_required
def admin_member(page_num):
	print('admin_member(), page_num: %d' % (page_num))

	count_per_page = 10
	member_all = models.Member.query.all()
	member_count = len(member_all)
	page_count = int((member_count-1) / count_per_page + 1)

	start_idx = (count_per_page * (page_num-1)) + 1
	end_idx = (count_per_page * (page_num-1)) + count_per_page
	if member_count < end_idx:
		end_idx = member_count

	member_page = []
	idx = 1
	for item in member_all:
		if start_idx <= idx and idx <= end_idx:
			member_page.append(item)
		idx += 1

	print('admin_member(), member_count: %d, page_count: %d' % (member_count, page_count))
	
	return render_template("admin_member.html", page_num = page_num, page_count = page_count, member_count = member_count, member_page = member_page, start_idx = start_idx, end_idx = end_idx)

@app.route('/admin_member/new', methods=['GET', 'POST'])
@flask_login.login_required
def admin_member_new():
	
	name = request.form['name']
	email = request.form['email']
	student_id = request.form['student_id']
	course = request.form['course']
	picture_path = request.form['picture_path']
	introduction = request.form['introduction']
	bd = request.form['bd']
	md = request.form['md']
	career1 = request.form['career1']
	career2 = request.form['career2']
	career3 = request.form['career3']
	link_github = request.form['link_github']
	link_facebook = request.form['link_facebook']
	link_twitter = request.form['link_twitter']
	link_linkedin = request.form['link_linkedin']
	link1 = request.form['link1']
	link2 = request.form['link2']
	link3 = request.form['link3']
	link4 = request.form['link4']

	print('admin_member_new(), name: %s, email: %s, student_id: %s' % (name, email, student_id))

	db_wrapper.insert_member(name=name, email=email, student_id=student_id, course=course, picture_path=picture_path, introduction=introduction, bd=bd, md=md, career1=career1, career2=career2, career3=career3, link_github=link_github, link_facebook=link_facebook, link_twitter=link_twitter, link_linkedin=link_linkedin, link1=link1, link2=link2, link3=link3, link4=link4)

	return redirect(url_for('admin_member', page_num=1))

@app.route('/admin_member/edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_member_edit():

	print('admin_member_edit()')
	
	member_id = request.form['member_id']
	name = request.form['name']
	email = request.form['email']
	student_id = request.form['student_id']
	course = request.form['course']
	picture_path = request.form['picture_path']
	introduction = request.form['introduction']
	bd = request.form['bd']
	md = request.form['md']
	career1 = request.form['career1']
	career2 = request.form['career2']
	career3 = request.form['career3']
	link_github = request.form['link_github']
	link_facebook = request.form['link_facebook']
	link_twitter = request.form['link_twitter']
	link_linkedin = request.form['link_linkedin']
	link1 = request.form['link1']
	link2 = request.form['link2']
	link3 = request.form['link3']
	link4 = request.form['link4']
	
	print('admin_member_edit(), title: %s, text1: %s, text2: %s' % (title, text1, text2))

	db_wrapper.update_member(name=name, email=email, student_id=student_id, course=course, picture_path=picture_path, introduction=introduction, bd=bd, md=md, career1=career1, career2=career2, career3=career3, link_github=link_github, link_facebook=link_facebook, link_twitter=link_twitter, link_linkedin=link_linkedin, link1=link1, link2=link2, link3=link3, link4=link4)

	return redirect(url_for('admin_member', page_num=1))

@app.route('/admin_member/delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_member_delete():

	print('admin_member_delete()')
	
	member_id = request.form['member_id']
	
	print('admin_member_delete(), member_id: %s' % (member_id))

	db_wrapper.delete_member(in_member_id = member_id)

	return redirect(url_for('admin_member', page_num=1))

@app.route('/admin_teaching/<int:page_num>')
@flask_login.login_required
def admin_teaching(page_num):
	
	print('admin_teaching(), page_num: %d' % (page_num))

	count_per_page = 10
	teaching_all = models.Teaching.query.all()
	teaching_count = len(teaching_all)
	page_count = int((teaching_count-1) / count_per_page + 1)

	start_idx = (count_per_page * (page_num-1)) + 1
	end_idx = (count_per_page * (page_num-1)) + count_per_page
	if teaching_count < end_idx:
		end_idx = teaching_count

	teaching_page = []
	idx = 1
	for item in teaching_all:
		if start_idx <= idx and idx <= end_idx:
			teaching_page.append(item)
		idx += 1

	print('admin_teaching(), teaching_count: %d, page_count: %d' % (teaching_count, page_count))
	
	return render_template("admin_teaching.html", page_num = page_num, page_count = page_count, teaching_count = teaching_count, teaching_page = teaching_page, start_idx = start_idx, end_idx = end_idx)

@app.route('/admin_teaching/new', methods=['GET', 'POST'])
@flask_login.login_required
def admin_teaching_new():
	
	code = request.form['code']
	name = request.form['name']
	description = request.form['description']
	when = request.form['when']
	target_audience = request.form['target_audience']
	link1 = request.form['link1']
	link2 = request.form['link2']

	print('admin_teaching_new(), code: %s, name: %s' % (code, name))

	db_wrapper.insert_teaching(code=code, name=name, description=description, when=when, target_audience=target_audience, link1=link1, link2=link2)

	return redirect(url_for('admin_teaching', page_num=1))

@app.route('/admin_teaching/edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_teaching_edit():

	print('admin_teaching_edit()')
	
	teaching_id = request.form['teaching_id']
	code = request.form['code']
	name = request.form['name']
	description = request.form['description']
	when = request.form['when']
	target_audience = request.form['target_audience']
	link1 = request.form['link1']
	link2 = request.form['link2']
	
	print('admin_teaching_edit(), code: %s, name: %s' % (code, name))

	db_wrapper.update_teaching(teaching_id=teaching_id, code=code, name=name, description=description, when=when, target_audience=target_audience, link1=link1, link2=link2)

	return redirect(url_for('admin_teaching', page_num=1))

@app.route('/admin_teaching/delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_teaching_delete():

	print('admin_teaching_delete()')
	
	teaching_id = request.form['teaching_id']
	
	print('admin_teaching_delete(), teaching_id: %s' % (teaching_id))

	db_wrapper.delete_teaching(in_teaching_id = teaching_id)

	return redirect(url_for('admin_teaching', page_num=1))

@app.route('/admin_publication/<int:page_num>')
@flask_login.login_required
def admin_publication(page_num):
	
	print('admin_publication(), page_num: %d' % (page_num))

	count_per_page = 10
	publication_all = models.Publications.query.all()
	publication_count = len(publication_all)
	page_count = int((publication_count-1) / count_per_page + 1)

	start_idx = (count_per_page * (page_num-1)) + 1
	end_idx = (count_per_page * (page_num-1)) + count_per_page
	if publication_count < end_idx:
		end_idx = publication_count

	publication_page = []
	idx = 1
	for item in publication_all:
		if start_idx <= idx and idx <= end_idx:
			publication_page.append(item)
		idx += 1

	print('admin_publication(), publication_count: %d, page_count: %d' % (publication_count, page_count))
	
	return render_template("admin_publication.html", page_num = page_num, page_count = page_count, publication_count = publication_count, publication_page = publication_page, start_idx = start_idx, end_idx = end_idx)

@app.route('/admin_publication/new', methods=['GET', 'POST'])
@flask_login.login_required
def admin_publication_new():
	
	title = request.form['title']
	conference = request.form['conference']
	abstract = request.form['abstract']
	teaser_image_path = request.form['teaser_image_path']
	authors = request.form['authors']
	link_pdf1 = request.form['link_pdf1']
	# link_pdf2 = request.form['link_pdf2']
	link_video = request.form['link_video']
	link_source = request.form['link_source']
	link_url = request.form['link_url']
	# link_etc = request.form['link_etc']
	
	print('admin_publication_new(), title: %s, conference: %s' % (title, conference))

	# db_wrapper.insert_publication(title=title, conference=conference, abstract=abstract, teaser_image_path=teaser_image_path, authors=authors, link_pdf1=link_pdf1, link_pdf2=link_pdf2, link_video=link_video, link_source=link_source, link_url=link_url, link_etc=link_etc)
	db_wrapper.insert_publication(title=title, conference=conference, abstract=abstract, teaser_image_path=teaser_image_path, authors=authors, link_pdf1=link_pdf1, link_video=link_video, link_source=link_source, link_url=link_url)

	return redirect(url_for('admin_publication', page_num=1))

@app.route('/admin_publication/edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_publication_edit():

	print('admin_publication_edit()')
	
	publication_id = request.form['publication_id']
	title = request.form['title']
	conference = request.form['conference']
	abstract = request.form['abstract']
	teaser_image_path = request.form['teaser_image_path']
	authors = request.form['authors']
	link_pdf1 = request.form['link_pdf1']
	# link_pdf2 = request.form['link_pdf2']
	link_video = request.form['link_video']
	link_source = request.form['link_source']
	link_url = request.form['link_url']
	# link_etc = request.form['link_etc']
	
	print('admin_publication_edit(), title: %s, conference: %s' % (title, conference))

	# db_wrapper.update_publication(publication_id=publication_id, title=title, conference=conference, abstract=abstract, teaser_image_path=teaser_image_path, authors=authors, link_pdf1=link_pdf1, link_pdf2=link_pdf2, link_video=link_video, link_source=link_source, link_url=link_url, link_etc=link_etc)
	db_wrapper.update_publication(id=publication_id, title=title, conference=conference, abstract=abstract, teaser_image_path=teaser_image_path, authors=authors, link_pdf1=link_pdf1, link_video=link_video, link_source=link_source, link_url=link_url)

	return redirect(url_for('admin_publication', page_num=1))

@app.route('/admin_publication/delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_publication_delete():

	print('admin_publication_delete()')
	
	publication_id = request.form['publication_id']
	
	print('admin_publication_delete(), publication_id: %s' % (publication_id))

	db_wrapper.delete_publication(id=publication_id)

	return redirect(url_for('admin_publication', page_num=1))

@app.route('/protected')
@flask_login.login_required
def protected():
    # return 'Logged in as: ' + flask_login.current_user.id
    return render_template("admin_title.html")

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('admin'))

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