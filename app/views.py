# coding: utf-8
from app import app
from flask import render_template, redirect, url_for, request
import flask_login
import os
from shutil import copyfile
from app import db, models, db_wrapper
from sqlalchemy import desc
from datetime import datetime

# Our mock database.
users = {'davian': {'pw': 'visualking!'}}

# category = {'news', 'people', 'publications', 'research', 'teaching', 'links'}

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
	
	labinfo = models.LabInfo.query.filter_by(id = 1).first()
	about = models.About.query.filter_by(id = 1).first()
	news = models.News.query.filter_by(show=True).order_by(desc(models.News.sn)).all()
	people = models.Member.query.filter_by(show=True).order_by(desc(models.Member.sn)).all()
	teaching = models.Teaching.query.filter_by(show=True).order_by(desc(models.Teaching.sn)).all()
	publications = models.Publications.query.filter_by(show=True).order_by(desc(models.Publications.sn)).all()
	links = models.Links.query.filter_by(show=True).order_by(desc(models.Links.sn)).all()

	bg = labinfo.background_img_path

	return render_template("index.html",
							labinfo=labinfo, 
							# about=about, 
							news=news,
							people=people, 
							bg=bg,
							teaching=teaching,
							publications=publications, 
							links=links)

@app.route('/member_page/<member_name>')
def member_page(member_name):
	file_dir = './app/templates/member_page'
	filename = "%s/%s.html" % (file_dir, member_name)
	if not os.path.exists(filename):
		copyfile('%s/template.html' % file_dir, filename)
	
	return render_template('member_page/%s.html' % member_name)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	if request.method == 'GET':
		return render_template("login.html")

	user_id = request.form.get('user_id').lower()
	if request.form.get('pw') == users[user_id]['pw']:
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
	
	print(labinfo.background_img_path)
	
	return render_template("admin_title.html", description=labinfo.description, 
		sub_description=labinfo.sub_description, bg_filename=labinfo.background_img_path)

@app.route('/admin_title_submit', methods=['GET','POST'])
@flask_login.login_required
def admin_title_submit():

	desc_text = request.form.get('description')
	subdesc_text = request.form.get('sub_description')
	background_filename = request.form.get('bg_filename')
	background_image = request.files.get('bg_image')

	print('admin_title_submit(), description: %s, sub_description: %s, bg_filename: %s' % (desc_text, subdesc_text, background_filename))

	db_wrapper.update_lab_info(desc = desc_text, 
		sub_desc = subdesc_text, bg_filename = background_filename, bg_image = background_image)

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
	
	text = request.form.get('about_text')
	sub_text = request.form.get('about_sub_text')

	print('admin_about_submit(), text: %s, sub_text: %s' % (text, sub_text))

	db_wrapper.update_about(text = text, sub_text = sub_text)

	return redirect(url_for('admin_about'))

@app.route('/admin_news/<int:page_num>')
@flask_login.login_required
def admin_news(page_num):

	print('admin_news(), page_num: %d' % (page_num))

	count_per_page = 10
	items = models.News.query.order_by(desc(models.News.sn)).all()
	item_count = len(items)
	page_count = int((item_count-1) / count_per_page + 1)

	today = datetime.now().strftime('%Y-%m-%d')

	start_idx = (count_per_page * (page_num-1)) + 1
	end_idx = (count_per_page * (page_num-1)) + count_per_page
	if item_count < end_idx:
		end_idx = item_count

	item_page = []
	idx = 1
	for item in items:
		if start_idx <= idx and idx <= end_idx:
			item_page.append(item)
		idx += 1

	print('admin_news(), item_count: %d, page_count: %d' % (item_count, page_count))
	
	return render_template("admin_news.html", page_num = page_num, page_count = page_count, item_count = item_count, item_page = item_page, start_idx = start_idx, end_idx = end_idx, today=today)

@app.route('/admin_news/admin_news_create_new', methods=['GET', 'POST'])
@flask_login.login_required
def admin_news_create_new():
	
	title = request.form.get('title')
	contents = request.form.get('contents')
	date = request.form.get('date')
	show = request.form.get('show') != None

	print('admin_news_create_new(), title: %s, contents: %s, date: %s, show: %s' % (title, contents, date, show))

	db_wrapper.insert_news(title=title, contents=contents, date=date, show=show)

	return redirect(url_for('admin_news', page_num=1))

@app.route('/admin_news/admin_news_edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_news_edit():

	print('admin_news_edit()')
	
	id = request.form.get('id')
	title = request.form.get('title')
	contents = request.form.get('contents')
	date = request.form.get('date')
	show = request.form.get('show') != None

	print('admin_news_edit(), title: %s, contents: %s, date: %s, show: %s' % (title, contents, date, show))

	db_wrapper.update_news(id = id,  title=title,  contents=contents,  date=date, show=show)

	return redirect(url_for('admin_news', page_num=1))

@app.route('/admin_news/admin_news_delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_news_delete():

	id = request.form.get('id')
	
	print('admin_news_delete(), id: %s' % id)

	db_wrapper.delete_item(category='news', id=id)

	return redirect(url_for('admin_news', page_num=1))

@app.route('/admin_news/admin_news_arrow/<int:id>/<int:sn>/<string:direction>')
@flask_login.login_required
def admin_news_arrow(id, sn, direction):

	print('admin_news_arrow(%d, %s)' % (sn, direction))

	db_wrapper.change_position(category='news', sn=sn, direction=direction)

	return redirect(url_for('admin_news', page_num=1))

@app.route('/admin_news/admin_news_toggle_show/<int:id>')
@flask_login.login_required
def admin_news_toggle_show(id):

	print('admin_news_toggle_show(%d)' % (id))

	db_wrapper.toggle_show(category='news', id=id)

	return redirect(url_for('admin_news', page_num=1))

@app.route('/admin_research/<int:page_num>')
@flask_login.login_required
def admin_research(page_num):
	
	print('admin_research(), page_num: %d' % (page_num))

	count_per_page = 10
	research_all = models.Research.query.order_by(desc(models.Research.sn)).all()
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

	title = request.form.get('title')
	text1 = request.form.get('text1')
	text2 = request.form.get('text2')
	teaser_image_path = request.form.get('teaser_image')
	member = request.form.get('member')
	publications = request.form.get('publications')
	is_activated = request.form.get('is_activated')
	show = request.form.get('show') != None

	print('admin_research_create_new(), title: %s, text1: %s, text2: %s' % (title, text1, text2))

	db_wrapper.insert_research(title=title, text1=text1, text2=text2, teaser_image_path=teaser_image_path, member=member, publications=publications, is_activated=is_activated, show=show)

	return redirect(url_for('admin_research', page_num=1))

@app.route('/admin_research/edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_research_edit():

	print('admin_research_edit()')
	
	research_id = request.form.get('research_id')
	title = request.form.get('title')
	text1 = request.form.get('text1')
	text2 = request.form.get('text2')
	teaser_image_path = request.form.get('teaser_image')
	member = request.form.get('member')
	publications = request.form.get('publications')
	is_activated = request.form.get('is_activated')
	show = request.form.get('show') != None
	
	print('admin_research_edit(), title: %s, text1: %s, text2: %s' % (title, text1, text2))

	db_wrapper.update_research(id=research_id, title=title, text1=text1, text2=text2, teaser_image_path=teaser_image_path, member=member, publications=publications, is_activated=is_activated, show=show)

	return redirect(url_for('admin_research', page_num=1))

@app.route('/admin_research/delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_research_delete():
	
	id = request.form.get('research_id')
	
	print('admin_research_delete(), id: %s' % (id))

	db_wrapper.delete_item(category='research', id=id)

	return redirect(url_for('admin_research', page_num=1))

@app.route('/admin_research/admin_research_arrow/<int:id>/<int:sn>/<string:direction>')
@flask_login.login_required
def admin_research_arrow(id, sn, direction):

	print('admin_research_arrow(%d, %s)' % (sn, direction))

	db_wrapper.change_position(category='research', sn=sn, direction=direction)

	return redirect(url_for('admin_research', page_num=1))

@app.route('/admin_research/admin_research_toggle_show/<int:id>')
@flask_login.login_required
def admin_research_toggle_show(id):

	print('admin_research_toggle_show(%d)' % (id))

	db_wrapper.toggle_show(category='research', id=id)

	return redirect(url_for('admin_research', page_num=1))

@app.route('/admin_member/<int:page_num>')
@flask_login.login_required
def admin_member(page_num):
	print('admin_member(), page_num: %d' % (page_num))

	count_per_page = 10
	member_all = models.Member.query.order_by(desc(models.Member.sn)).all()
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
	
	name = request.form.get('name')
	email = request.form.get('email')
	student_id = request.form.get('student_id')
	course = request.form.get('course')
	picture = request.files.get('picture')
	interest = request.form.get('interest')
	bs = request.form.get('bs')
	ms = request.form.get('ms')
	introduction = request.form.get('introduction')
	# career2 = request.form.get('career2')
	# career3 = request.form.get('career3')
	link_github = request.form.get('link_github')
	link_facebook = request.form.get('link_facebook')
	link_twitter = request.form.get('link_twitter')
	link_linkedin = request.form.get('link_linkedin')
	# link1 = request.form.get('link1')
	# link2 = request.form.get('link2')
	# link3 = request.form.get('link3')
	# link4 = request.form.get('link4')
	show = request.form.get('show') != None

	print('admin_member_new(), name: %s, email: %s, student_id: %s' % (name, email, student_id))

	db_wrapper.insert_member(name=name, email=email, student_id=student_id, course=course, picture=picture, interest=interest, bs=bs, ms=ms, introduction=introduction, link_github=link_github, link_facebook=link_facebook, link_twitter=link_twitter, link_linkedin=link_linkedin, show=show)

	return redirect(url_for('admin_member', page_num=1))

@app.route('/admin_member/edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_member_edit():

	print('admin_member_edit()')
	
	member_id = request.form.get('member_id')
	name = request.form.get('name')
	email = request.form.get('email')
	student_id = request.form.get('student_id')
	course = request.form.get('course')
	picture_filename = request.form.get('picture_filename')
	picture = request.files.get('picture')
	introduction = request.form.get('introduction')
	interest = request.form.get('interest')
	bs = request.form.get('bs')
	ms = request.form.get('ms')
	introduction = request.form.get('introduction')
	# career1 = request.form.get('career1')
	# career2 = request.form.get('career2')
	# career3 = request.form.get('career3')
	link_homepage = request.form.get('link_homepage')
	link_github = request.form.get('link_github')
	link_facebook = request.form.get('link_facebook')
	link_twitter = request.form.get('link_twitter')
	link_linkedin = request.form.get('link_linkedin')
	# link1 = request.form.get('link1')
	# link2 = request.form.get('link2')
	# link3 = request.form.get('link3')
	# link4 = request.form.get('link4')
	show = request.form.get('show') != None
	
	print('admin_member_edit(), name: %s, student_id: %s, email: %s' % (name, student_id, email))

	db_wrapper.update_member(id=member_id, name=name, email=email, student_id=student_id, course=course, picture_filename=picture_filename, picture=picture, interest=interest, bs=bs, ms=ms, introduction=introduction, link_homepage=link_homepage, link_github=link_github, link_facebook=link_facebook, link_twitter=link_twitter, link_linkedin=link_linkedin, show=show)

	return redirect(url_for('admin_member', page_num=1))

@app.route('/admin_member/delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_member_delete():

	id = request.form.get('member_id')
	
	print('admin_member_delete(), id: %s' % (id))

	db_wrapper.delete_item(category='people', id=id)

	return redirect(url_for('admin_member', page_num=1))

@app.route('/admin_member/admin_member_arrow/<int:id>/<int:sn>/<string:direction>')
@flask_login.login_required
def admin_member_arrow(id, sn, direction):

	print('admin_member_arrow(%d, %s)' % (sn, direction))

	db_wrapper.change_position(category='people', sn=sn, direction=direction)

	return redirect(url_for('admin_member', page_num=1))

@app.route('/admin_member/admin_member_toggle_show/<int:id>')
@flask_login.login_required
def admin_member_toggle_show(id):

	print('admin_member_toggle_show(%d)' % (id))

	db_wrapper.toggle_show(category='people', id=id)

	return redirect(url_for('admin_member', page_num=1))

@app.route('/admin_teaching/<int:page_num>')
@flask_login.login_required
def admin_teaching(page_num):
	
	print('admin_teaching(), page_num: %d' % (page_num))

	count_per_page = 10
	teaching_all = models.Teaching.query.order_by(desc(models.Teaching.sn)).all()
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
	
	code = request.form.get('code')
	name = request.form.get('name')
	description = request.form.get('description')
	when = request.form.get('when')
	target_audience = request.form.get('target_audience')
	link = request.form.get('link')
	video = request.form.get('video')
	show = request.form.get('show') != None

	print('admin_teaching_new(), code: %s, name: %s' % (code, name))

	db_wrapper.insert_teaching(code=code, name=name, description=description, when=when, target_audience=target_audience, link=link, video=video, show=show)

	return redirect(url_for('admin_teaching', page_num=1))

@app.route('/admin_teaching/edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_teaching_edit():

	print('admin_teaching_edit()')
	
	teaching_id = request.form.get('teaching_id')
	code = request.form.get('code')
	name = request.form.get('name')
	description = request.form.get('description')
	when = request.form.get('when')
	target_audience = request.form.get('target_audience')
	link = request.form.get('link')
	video = request.form.get('video')
	show = request.form.get('show') != None
	
	print('admin_teaching_edit(), id: %d. code: %s, name: %s, audience:%s ' % (int(teaching_id), code, name, target_audience))

	db_wrapper.update_teaching(id=teaching_id, code=code, name=name, description=description, when=when, target_audience=target_audience, link=link, video=video, show=show)

	return redirect(url_for('admin_teaching', page_num=1))

@app.route('/admin_teaching/delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_teaching_delete():
	
	id = request.form.get('teaching_id')
	
	print('admin_teaching_delete(), id: %s' % (id))

	db_wrapper.delete_item(category='teaching', id=id)

	return redirect(url_for('admin_teaching', page_num=1))

@app.route('/admin_teaching/admin_teaching_arrow/<int:id>/<int:sn>/<string:direction>')
@flask_login.login_required
def admin_teaching_arrow(id, sn, direction):

	print('admin_teaching_arrow(%d, %s)' % (sn, direction))

	db_wrapper.change_position(category='teaching', sn=sn, direction=direction)

	return redirect(url_for('admin_teaching', page_num=1))

@app.route('/admin_teaching/admin_teaching_toggle_show/<int:id>')
@flask_login.login_required
def admin_teaching_toggle_show(id):

	print('admin_teaching_toggle_show(%d)' % (id))

	db_wrapper.toggle_show(category='teaching', id=id)

	return redirect(url_for('admin_teaching', page_num=1))

@app.route('/admin_publication/<int:page_num>')
@flask_login.login_required
def admin_publication(page_num):
	
	print('admin_publication(), page_num: %d' % (page_num))

	count_per_page = 10
	publication_all = models.Publications.query.order_by(desc(models.Publications.sn)).all()
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
	
	title = request.form.get('title')
	description = request.form.get('description')
	year = request.form.get('year')
	abstract = request.form.get('abstract')
	teaser_image = request.files.get('teaser_image')
	authors = request.form.get('authors')
	link_pdf1 = request.form.get('link_pdf1')
	# link_pdf2 = request.form.get('link_pdf2')
	link_video = request.form.get('link_video')
	link_source = request.form.get('link_source')
	link_url = request.form.get('link_url')
	# link_etc = request.form.get('link_etc')
	# is_activated = request.form.get('is_activated')
	show = request.form.get('show') != None
	
	print('admin_publication_new(), title: %s, description: %s' % (title, description))

	# db_wrapper.insert_publication(title=title, description=description, abstract=abstract, teaser_image_path=teaser_image_path, authors=authors, link_pdf1=link_pdf1, link_pdf2=link_pdf2, link_video=link_video, link_source=link_source, link_url=link_url, link_etc=link_etc)
	db_wrapper.insert_publication(title=title, description=description, year=year, abstract=abstract, teaser_image=teaser_image, authors=authors, link_pdf1=link_pdf1, link_video=link_video, link_source=link_source, link_url=link_url, show=show)

	return redirect(url_for('admin_publication', page_num=1))

@app.route('/admin_publication/edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_publication_edit():

	print('admin_publication_edit()')
	
	publication_id = request.form.get('publication_id')
	title = request.form.get('title')
	description = request.form.get('description')
	year = request.form.get('year')
	abstract = request.form.get('abstract')
	teaser_filename = request.form.get('teaser_filename')
	teaser_image = request.files.get('teaser_image')
	authors = request.form.get('authors')
	link_pdf1 = request.form.get('link_pdf1')
	# link_pdf2 = request.form.get('link_pdf2')
	link_video = request.form.get('link_video')
	link_source = request.form.get('link_source')
	link_url = request.form.get('link_url')
	# link_etc = request.form.get('link_etc')
	show = request.form.get('show') != None
	
	print('admin_publication_edit(), title: %s, description: %s' % (title, description))

	# db_wrapper.update_publication(publication_id=publication_id, title=title, description=description, abstract=abstract, teaser_image_path=teaser_image_path, authors=authors, link_pdf1=link_pdf1, link_pdf2=link_pdf2, link_video=link_video, link_source=link_source, link_url=link_url, link_etc=link_etc)
	db_wrapper.update_publication(id=publication_id, title=title, description=description, year=year, abstract=abstract, teaser_filename=teaser_filename, teaser_image=teaser_image, authors=authors, link_pdf1=link_pdf1, link_video=link_video, link_source=link_source, link_url=link_url, show=show)

	return redirect(url_for('admin_publication', page_num=1))

@app.route('/admin_publication/delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_publication_delete():

	id = request.form.get('publication_id')
	
	print('admin_publication_delete(), id: %s' % (id))

	db_wrapper.delete_item(category='publications', id=id)

	return redirect(url_for('admin_publication', page_num=1))

@app.route('/admin_publication/admin_publication_arrow/<int:id>/<int:sn>/<string:direction>')
@flask_login.login_required
def admin_publication_arrow(id, sn, direction):

	print('admin_publication_arrow(%d, %s)' % (sn, direction))

	db_wrapper.change_position(category='publications', sn=sn, direction=direction)

	return redirect(url_for('admin_publication', page_num=1))

@app.route('/admin_publication/admin_publication_toggle_show/<int:id>')
@flask_login.login_required
def admin_publication_toggle_show(id):

	print('admin_publication_toggle_show(%d)' % (id))

	db_wrapper.toggle_show(category='publications', id=id)

	return redirect(url_for('admin_publication', page_num=1))

@app.route('/admin_links/<int:page_num>')
@flask_login.login_required
def admin_links(page_num):
	
	print('admin_links(), page_num: %d' % (page_num))

	count_per_page = 10
	links_all = models.Links.query.order_by(desc(models.Links.sn)).all()
	links_count = len(links_all)
	page_count = int((links_count-1) / count_per_page + 1)

	start_idx = (count_per_page * (page_num-1)) + 1
	end_idx = (count_per_page * (page_num-1)) + count_per_page
	if links_count < end_idx:
		end_idx = links_count

	links_page = []
	idx = 1
	for item in links_all:
		if start_idx <= idx and idx <= end_idx:
			links_page.append(item)
		idx += 1

	print('admin_links(), links_count: %d, page_count: %d' % (links_count, page_count))
	
	return render_template("admin_links.html", page_num = page_num, page_count = page_count, links_count = links_count, links_page = links_page, start_idx = start_idx, end_idx = end_idx)

@app.route('/admin_links/new', methods=['GET', 'POST'])
@flask_login.login_required
def admin_links_new():
	
	name = request.form.get('name')
	description = request.form.get('description')
	image_path = request.files.get('image_path')
	link_url = request.form.get('link_url')
	link_etc = request.form.get('link_etc')
	# is_activated = request.form.get('is_activated')
	show = request.form.get('show') != None
	
	print('admin_links_new(), name: %s, description: %s' % (name, description))


	db_wrapper.insert_link(name=name, description=description, image_path=image_path, link_url=link_url, link_etc=link_etc, show=show)

	return redirect(url_for('admin_links', page_num=1))

@app.route('/admin_links/edit', methods=['GET', 'POST'])
@flask_login.login_required
def admin_links_edit():

	print('admin_links_edit()')
	
	link_id = request.form.get('link_id')
	name = request.form.get('name')
	description = request.form.get('description')
	image_name = request.files.get('image_name')
	image_path = request.files.get('image_path')
	link_url = request.form.get('link_url')
	link_etc = request.form.get('link_etc')

	show = request.form.get('show') != None
	
	print('admin_links_edit(), name: %s, description: %s, image_path: %s' % (name, description, image_path))

	# db_wrapper.update_links(links_id=links_id, title=title, description=description, abstract=abstract, teaser_image_path=teaser_image_path, authors=authors, link_pdf1=link_pdf1, link_pdf2=link_pdf2, link_video=link_video, link_source=link_source, link_url=link_url, link_etc=link_etc)
	db_wrapper.update_link(id=link_id, name=name, description=description, image_name=image_name, image_path=image_path, link_url=link_url, link_etc=link_etc, show=show)

	return redirect(url_for('admin_links', page_num=1))

@app.route('/admin_links/delete', methods=['GET', 'POST'])
@flask_login.login_required
def admin_links_delete():
	
	id = request.form.get('link_id')
	
	print('admin_links_delete(), id: %s' % (id))

	db_wrapper.delete_item(category='links', id=id)

	db_wrapper.delete_link(id=link_id)

	return redirect(url_for('admin_links', page_num=1))

@app.route('/admin_links/admin_links_arrow/<int:id>/<int:sn>/<string:direction>')
@flask_login.login_required
def admin_links_arrow(id, sn, direction):

	print('admin_links_arrow(%d, %s)' % (sn, direction))

	db_wrapper.change_position(category='links', sn=sn, direction=direction)

	return redirect(url_for('admin_links', page_num=1))

@app.route('/admin_links/admin_links_toggle_show/<int:id>')
@flask_login.login_required
def admin_links_toggle_show(id):

	print('admin_links_toggle_show(%d)' % (id))

	db_wrapper.toggle_show(category='links', id=id)

	return redirect(url_for('admin_links', page_num=1))

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
    user.is_authenticated = request.form.get('pw') == users[user_id]['pw']

    return user

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'