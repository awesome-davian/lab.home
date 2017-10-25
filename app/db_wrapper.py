import os
from app import app, db, models
from werkzeug.utils import secure_filename
from datetime import datetime

def update_lab_info(in_desc, in_sub_desc, in_bg_image):

	bg_name = secure_filename(in_bg_image.filename)

	if bg_name != '':
		
		bg_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/')
		bg_path = os.path.join(bg_path, bg_name)
		
		print(bg_path)
		in_bg_image.save(bg_path)

	labinfo = models.LabInfo.query.filter_by(id = 1)
	if labinfo != None:
		labinfo.update(dict(description=in_desc))
		labinfo.update(dict(sub_description=in_sub_desc))
		if bg_name != '':
			labinfo.update(dict(background_img_path=bg_path))
		db.session.commit()
	else:
		print('labinfo == None')

def update_about(in_text, in_sub_text):

	about = models.About.query.filter_by(id = 1)
	print(about)
	if about != None:
		print('about != None')
		about.update(dict(text=in_text))
		about.update(dict(sub_text=in_sub_text))
		
		db.session.commit()
	else:
		print('about == None')

def insert_news(in_news_title, in_news_contents, in_news_date):

	date_in_python = datetime.strptime(in_news_date, '%Y-%m-%d')

	news = models.News(title=in_news_title, contents=in_news_contents, date=date_in_python)
	db.session.add(news)
	db.session.commit()

def update_news(in_news_id, in_news_title, in_news_contents, in_news_date):

	date_in_python = datetime.strptime(in_news_date, '%Y-%m-%d')

	news = models.News.query.filter_by(id=int(in_news_id))
	print(news)
	if news != None:
		print('news != None')
		news.update(dict(title=in_news_title))
		news.update(dict(contents=in_news_contents))
		news.update(dict(date=date_in_python))
		
		db.session.commit()
	else:
		print('news == None')

def delete_news(in_news_id):

	news = models.News.query.filter_by(id=int(in_news_id)).first()
	if news != None:
		db.session.delete(news)
		db.session.commit()
	else:
		print('news == None')

def insert_research(title, text1, text2, teaser_image_path, member, publications, is_activated):

	research = models.Research(title=title, text1=text1, text2=text2, teaser_image_path=teaser_image_path, member=member, publications=publications, is_activated=is_activated)
	db.session.add(research)
	db.session.commit()

def update_research(id, title, text1, text2, teaser_image_path, member, publications, is_activated):

	research = models.Research.query.filter_by(id=int(id))
	# print(research)
	if research != None:
		print('research != None')
		research.update(dict(title=title))
		research.update(dict(text1=text1))
		research.update(dict(text2=text2))
		research.update(dict(teaser_image_path=teaser_image_path))
		research.update(dict(member=member))
		research.update(dict(publications=publications))
		research.update(dict(is_activated=is_activated))
		
		db.session.commit()
	else:
		print('research == None')

def delete_research(id):

	research = models.Research.query.filter_by(id=int(id)).first()
	if research != None:
		db.session.delete(research)
		db.session.commit()
	else:
		print('research == None')

def insert_member(name, email, student_id, course, picture_path, introduction, bd, md, career1, career2, career3, link_github, link_facebook, link_twitter, link_linkedin, link1, link2, link3, link4):

	member = models.Member(name=name, email=email, student_id=student_id, course=course, picture_path=picture_path, introduction=introduction, bd=bd, md=md, career1=career1, career2=career2, career3=career3, link_github=link_github, link_facebook=link_facebook, link_twitter=link_twitter, link_linkedin=link_linkedin, link1=link1, link2=link2, link3=link3, link4=link4)
	db.session.add(member)
	db.session.commit()

def update_member(id, name, email, student_id, course, picture_path, introduction, bd, md, career1, career2, career3, link_github, link_facebook, link_twitter, link_linkedin, link1, link2, link3, link4):

	member = models.Member.query.filter_by(id=int(id))
	
	if member != None:
		print('member != None')
		member.update(dict(title=title))
		member.update(dict(name=name))
		member.update(dict(email=email))
		member.update(dict(student_id=student_id))
		member.update(dict(course=course))
		member.update(dict(picture_path=picture_path))
		member.update(dict(introduction=introduction))
		member.update(dict(bd=bd))
		member.update(dict(md=md))
		member.update(dict(career1=career1))
		member.update(dict(career2=career2))
		member.update(dict(career3=career3))
		member.update(dict(link_github=link_github))
		member.update(dict(link_facebook=link_facebook))
		member.update(dict(link_twitter=link_twitter))
		member.update(dict(link_linkedin=link_linkedin))
		member.update(dict(link1=link1))
		member.update(dict(link2=link2))
		member.update(dict(link3=link3))
		member.update(dict(link4=link4))

		db.session.commit()
	else:
		print('member == None')

def delete_member(id):

	member = models.Member.query.filter_by(id=int(id)).first()
	if member != None:
		db.session.delete(member)
		db.session.commit()
	else:
		print('member == None')

def insert_teaching(code, name, description, when, target_audience, link1, link2):

	teaching = models.Teaching(code=code, name=name, description=description, when=when, target_audience=target_audience, link1=link1, link2=link2)
	db.session.add(teaching)
	db.session.commit()

def update_teaching(id, code, name, description, when, target_audience, link1, link2):

	teaching = models.Teaching.query.filter_by(id=int(id))
	
	if teaching != None:
		print('teaching != None')
		teaching.update(dict(code=code))
		teaching.update(dict(name=name))
		teaching.update(dict(description=description))
		teaching.update(dict(when=when))
		teaching.update(dict(target_audience=target_audience))
		teaching.update(dict(link1=link1))
		teaching.update(dict(link2=link2))

		db.session.commit()
	else:
		print('teaching == None')

def delete_teaching(id):

	teaching = models.Teaching.query.filter_by(id=int(id)).first()
	if teaching != None:
		db.session.delete(teaching)
		db.session.commit()
	else:
		print('teaching == None')

# def insert_publication(title, conference, abstract, teaser_image_path, authors, link_pdf1, link_pdf2, link_video, link_source, link_url, link_etc):
def insert_publication(title, conference, abstract, teaser_image_path, authors, link_pdf1, link_video, link_source, link_url):

	# publications = models.Publications(title=title, conference=conference, abstract=abstract, teaser_image_path=teaser_image_path, authors=authors, link_pdf1=link_pdf1, link_pdf2=link_pdf2, link_video=link_video, link_source=link_source, link_url=link_url, link_etc=link_etc)
	publications = models.Publications(title=title, conference=conference, abstract=abstract, teaser_image_path=teaser_image_path, authors=authors, link_pdf1=link_pdf1, link_video=link_video, link_source=link_source, link_url=link_url)
	db.session.add(publications)
	db.session.commit()

# def update_publication(id, title, conference, abstract, teaser_image_path, authors, link_pdf1, link_pdf2, link_video, link_source, link_url, link_etc):
def update_publication(id, title, conference, abstract, teaser_image_path, authors, link_pdf1, link_video, link_source, link_url):

	publications = models.Publications.query.filter_by(id=int(id))
	
	if publications != None:
		print('publications != None')
		publications.update(dict(title=title))
		publications.update(dict(conference=conference))
		publications.update(dict(abstract=abstract))
		publications.update(dict(teaser_image_path=teaser_image_path))
		publications.update(dict(authors=authors))
		publications.update(dict(link_pdf1=link_pdf1))
		# publications.update(dict(link_pdf2=link_pdf2))
		publications.update(dict(link_video=link_video))
		publications.update(dict(link_source=link_source))
		publications.update(dict(link_url=link_url))
		# publications.update(dict(link_etc=link_etc))
		
		db.session.commit()
	else:
		print('publications == None')

def delete_publication(id):

	publications = models.Publications.query.filter_by(id=int(id)).first()
	if publications != None:
		db.session.delete(publications)
		db.session.commit()
	else:
		print('publications == None')


