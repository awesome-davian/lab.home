import os
from app import app, db, models
from werkzeug.utils import secure_filename
from datetime import datetime

def update_lab_info(desc, sub_desc, bg_filename, bg_image):

	bg_name = secure_filename(bg_image.filename)

	if bg_name != '':
		
		bg_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/')
		bg_path = os.path.join(bg_path, bg_name)
		
		print(bg_path)
		bg_image.save(bg_path)
	else:
		if bg_filename != '':
			bg_name = bg_filename
		else:
			# TODO: input default file
			bg_name = ''

	labinfo = models.LabInfo.query.filter_by(id = 1)
	if labinfo != None:
		if labinfo.count() != 0:
			labinfo.update(dict(description=desc))
			labinfo.update(dict(sub_description=sub_desc))
			if bg_name != '':
				labinfo.update(dict(background_img_path=bg_name))
		else:
			labinfo = models.LabInfo(name='DAVIAN', description=desc, sub_description=sub_desc, background_img_path=bg_name)
			db.session.add(labinfo)

		db.session.commit()
	else:
		print('labinfo == None')

def update_about(text, sub_text):

	about = models.About.query.filter_by(id = 1)
	print(about)
	if about != None:
		if about.count() != 0:
			about.update(dict(text=text))
			about.update(dict(sub_text=sub_text))
		else:
			about = models.About(text=text, sub_text=sub_text)
			db.session.add(about)
		
		db.session.commit()
	else:
		print('about == None')

def insert_news(title, contents, date, show):

	date_python = datetime.strptime(date, '%Y-%m-%d')

	news = models.News(title=title, contents=contents, date=date_python, show=show)
	db.session.add(news)
	db.session.commit()

def update_news(id, title, contents, date, show):

	date_python = datetime.strptime(date, '%Y-%m-%d')

	news = models.News.query.filter_by(id=int(id))
	print(news)
	if news != None:
		print('news != None')
		news.update(dict(title=title))
		news.update(dict(contents=contents))
		news.update(dict(date=date_python))
		news.update(dict(show=show))
		
		db.session.commit()
	else:
		print('news == None')

def delete_news(id):

	news = models.News.query.filter_by(id=int(id)).first()
	if news != None:
		db.session.delete(news)
		db.session.commit()
	else:
		print('news == None')

def news_arrow_up(id):

	idx = int(id)
	idx_next = idx+1
	temp = -1

	news = models.News.query.filter_by(id=idx).first()
	news_next = models.News.query.filter_by(id=idx_next).first()

	if news != None and news_next != None:
		models.News.query.filter_by(id=idx_next).update(dict(id=temp))
		models.News.query.filter_by(id=idx).update(dict(id=idx_next))
		models.News.query.filter_by(id=temp).update(dict(id=idx))

		db.session.commit()

	else:
		print('news == None || news_next == None')

def news_arrow_down(id):

	idx = int(id)
	idx_prev = idx-1
	temp = -1

	news = models.News.query.filter_by(id=idx).first()
	news_prev = models.News.query.filter_by(id=idx_prev).first()

	if news != None and news_prev != None:
		models.News.query.filter_by(id=idx_prev).update(dict(id=temp))
		models.News.query.filter_by(id=idx).update(dict(id=idx_prev))
		models.News.query.filter_by(id=temp).update(dict(id=idx))

		db.session.commit()

	else:
		print('news == None || news_prev == None')

def news_toggle_show(id):

	idx = int(id)
	news = models.News.query.filter_by(id=idx).first()

	print(news.show)

	if news != None:
		models.News.query.filter_by(id=idx).update(dict(show = (news.show == False)))
		db.session.commit()
	else:
		print('news == None')


def insert_research(title, text1, text2, teaser_image_path, member, publications, is_activated, show):

	research = models.Research(title=title, text1=text1, text2=text2, teaser_image_path=teaser_image_path, member=member, publications=publications, is_activated=is_activated, show=show)
	db.session.add(research)
	db.session.commit()

def update_research(id, title, text1, text2, teaser_image_path, member, publications, is_activated, show):

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
		research.update(dict(show=show))
		
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

def research_arrow_up(id):

	idx = int(id)
	idx_next = idx+1
	temp = -1

	research = models.Research.query.filter_by(id=idx).first()
	research_next = models.Research.query.filter_by(id=idx_next).first()

	if research != None and research_next != None:
		models.Research.query.filter_by(id=idx_next).update(dict(id=temp))
		models.Research.query.filter_by(id=idx).update(dict(id=idx_next))
		models.Research.query.filter_by(id=temp).update(dict(id=idx))

		db.session.commit()

	else:
		print('research == None || research_next == None')

def research_arrow_down(id):

	idx = int(id)
	idx_prev = idx-1
	temp = -1

	research = models.Research.query.filter_by(id=idx).first()
	research_prev = models.Research.query.filter_by(id=idx_prev).first()

	if research != None and research_prev != None:
		models.Research.query.filter_by(id=idx_prev).update(dict(id=temp))
		models.Research.query.filter_by(id=idx).update(dict(id=idx_prev))
		models.Research.query.filter_by(id=temp).update(dict(id=idx))

		db.session.commit()

	else:
		print('research == None || research_prev == None')

def research_toggle_show(id):

	idx = int(id)
	item = models.Research.query.filter_by(id=idx).first()

	print(item.show)

	if item != None:
		models.Research.query.filter_by(id=idx).update(dict(show = (item.show == False)))
		db.session.commit()
	else:
		print('item == None')

def insert_member(name, email, student_id, course, picture, interest, bs, ms, introduction, link_github, link_facebook, link_twitter, link_linkedin, show):

	picture_name = secure_filename(picture.filename)
	if picture_name != '':
		picture_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/member/')
		picture_path = os.path.join(picture_path, picture_name)
		
		print(picture_path)
		picture.save(picture_path)

	member = models.Member(name=name, email=email, student_id=student_id, course=course, picture_path=picture_name, interest=interest, bs=bs, ms=ms, introduction=introduction, link_github=link_github, link_facebook=link_facebook, link_twitter=link_twitter, link_linkedin=link_linkedin, show=show)
	db.session.add(member)
	db.session.commit()

def update_member(id, name, email, student_id, course, picture_filename, picture, interest, bs, ms, introduction, link_github, link_facebook, link_twitter, link_linkedin, show):

	picture_name = secure_filename(picture.filename)
	if picture_name != '':
		picture_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/member/')
		picture_path = os.path.join(picture_path, picture_name)
		
		print(picture_path)
		picture.save(picture_path)
	else:
		if picture_filename != '':
			picture_name = picture_filename
		else:
			picture_name = ''

	member = models.Member.query.filter_by(id=int(id))
	
	if member != None:
		print('member != None')
		member.update(dict(name=name))
		member.update(dict(email=email))
		member.update(dict(student_id=student_id))
		member.update(dict(course=course))
		member.update(dict(picture_path=picture_name))
		member.update(dict(interest=interest))
		member.update(dict(bs=bs))
		member.update(dict(ms=ms))
		member.update(dict(introduction=introduction))
		member.update(dict(link_github=link_github))
		member.update(dict(link_facebook=link_facebook))
		member.update(dict(link_twitter=link_twitter))
		member.update(dict(link_linkedin=link_linkedin))
		member.update(dict(show=show))

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

def member_arrow_up(id):

	idx = int(id)
	idx_next = idx+1
	temp = -1

	member = models.Member.query.filter_by(id=idx).first()
	member_next = models.Member.query.filter_by(id=idx_next).first()

	if member != None and member_next != None:
		models.Member.query.filter_by(id=idx_next).update(dict(id=temp))
		models.Member.query.filter_by(id=idx).update(dict(id=idx_next))
		models.Member.query.filter_by(id=temp).update(dict(id=idx))

		db.session.commit()

	else:
		print('member == None || member_next == None')

def member_arrow_down(id):

	idx = int(id)
	idx_prev = idx-1
	temp = -1

	member = models.Member.query.filter_by(id=idx).first()
	member_prev = models.Member.query.filter_by(id=idx_prev).first()

	if member != None and member_prev != None:
		models.Member.query.filter_by(id=idx_prev).update(dict(id=temp))
		models.Member.query.filter_by(id=idx).update(dict(id=idx_prev))
		models.Member.query.filter_by(id=temp).update(dict(id=idx))

		db.session.commit()

	else:
		print('member == None || member_prev == None')

def member_toggle_show(id):

	idx = int(id)
	item = models.Member.query.filter_by(id=idx).first()

	print(item.show)

	if item != None:
		models.Member.query.filter_by(id=idx).update(dict(show = (item.show == False)))
		db.session.commit()
	else:
		print('item == None')

def insert_teaching(code, name, description, when, target_audience, link, video, show):

	teaching = models.Teaching(code=code, name=name, description=description, when=when, target_audience=target_audience, link=link, video=video, show=show)
	db.session.add(teaching)
	db.session.commit()

def update_teaching(id, code, name, description, when, target_audience, link, video, show):

	teaching = models.Teaching.query.filter_by(id=int(id))
	
	if teaching != None:
		print('teaching != None')
		teaching.update(dict(code=code))
		teaching.update(dict(name=name))
		teaching.update(dict(description=description))
		teaching.update(dict(when=when))
		teaching.update(dict(target_audience=target_audience))
		teaching.update(dict(link=link))
		teaching.update(dict(video=video))
		teaching.update(dict(show=show))

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

def teaching_arrow_up(id):

	idx = int(id)
	idx_next = idx+1
	temp = -1

	teaching = models.Teaching.query.filter_by(id=idx).first()
	teaching_next = models.Teaching.query.filter_by(id=idx_next).first()

	if teaching != None and teaching_next != None:
		models.Teaching.query.filter_by(id=idx_next).update(dict(id=temp))
		models.Teaching.query.filter_by(id=idx).update(dict(id=idx_next))
		models.Teaching.query.filter_by(id=temp).update(dict(id=idx))

		db.session.commit()

	else:
		print('teaching == None || teaching_next == None')

def teaching_arrow_down(id):

	idx = int(id)
	idx_prev = idx-1
	temp = -1

	teaching = models.Teaching.query.filter_by(id=idx).first()
	teaching_prev = models.Teaching.query.filter_by(id=idx_prev).first()

	if teaching != None and teaching_prev != None:
		models.Teaching.query.filter_by(id=idx_prev).update(dict(id=temp))
		models.Teaching.query.filter_by(id=idx).update(dict(id=idx_prev))
		models.Teaching.query.filter_by(id=temp).update(dict(id=idx))

		db.session.commit()

	else:
		print('teaching == None || teaching_prev == None')

def teaching_toggle_show(id):

	idx = int(id)
	item = models.Teaching.query.filter_by(id=idx).first()

	print(item.show)

	if item != None:
		models.Teaching.query.filter_by(id=idx).update(dict(show = (item.show == False)))
		db.session.commit()
	else:
		print('item == None')

# def insert_publication(title, description, abstract, teaser_image_path, authors, link_pdf1, link_pdf2, link_video, link_source, link_url, link_etc):
def insert_publication(title, description, year, abstract, teaser_image, authors, link_pdf1, link_video, link_source, link_url, show):

	teaser_image_name = secure_filename(teaser_image.filename)
	if teaser_image_name != '':
		teaser_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/publications/')
		teaser_path = os.path.join(teaser_path, teaser_image_name)
		
		print(teaser_path)
		teaser_image.save(teaser_path)

	# publications = models.Publications(title=title, description=description, abstract=abstract, teaser_image_path=teaser_image_path, authors=authors, link_pdf1=link_pdf1, link_pdf2=link_pdf2, link_video=link_video, link_source=link_source, link_url=link_url, link_etc=link_etc)
	publications = models.Publications(title=title, description=description, year=year, abstract=abstract, teaser_image_path=teaser_image_name, authors=authors, link_pdf1=link_pdf1, link_video=link_video, link_source=link_source, link_url=link_url, show=show)
	db.session.add(publications)
	db.session.commit()

# def update_publication(id, title, description, abstract, teaser_image_path, authors, link_pdf1, link_pdf2, link_video, link_source, link_url, link_etc):
def update_publication(id, title, description, year, abstract, teaser_filename, teaser_image, authors, link_pdf1, link_video, link_source, link_url, show):

	teaser_image_name = secure_filename(teaser_image.filename)
	if teaser_image_name != '':
		teaser_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/publications/')
		teaser_path = os.path.join(teaser_path, teaser_image_name)
		
		print(teaser_path)
		teaser_image.save(teaser_path)
	else:
		if teaser_filename != '':
			teaser_image_name = teaser_filename
		else:
			teaser_image_name = ''

	publications = models.Publications.query.filter_by(id=int(id))
	
	if publications != None:
		print('publications != None')
		publications.update(dict(title=title))
		publications.update(dict(description=description))
		publications.update(dict(year=year))
		publications.update(dict(abstract=abstract))
		publications.update(dict(teaser_image_path=teaser_image_name))
		publications.update(dict(authors=authors))
		publications.update(dict(link_pdf1=link_pdf1))
		# publications.update(dict(link_pdf2=link_pdf2))
		publications.update(dict(link_video=link_video))
		publications.update(dict(link_source=link_source))
		publications.update(dict(link_url=link_url))
		# publications.update(dict(link_etc=link_etc))
		publications.update(dict(show=show))
		
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

def publication_arrow_up(id):

	idx = int(id)
	idx_next = idx+1
	temp = -1

	publication = models.publication.query.filter_by(id=idx).first()
	publication_next = models.publication.query.filter_by(id=idx_next).first()

	if publication != None and publication_next != None:
		models.publication.query.filter_by(id=idx_next).update(dict(id=temp))
		models.publication.query.filter_by(id=idx).update(dict(id=idx_next))
		models.publication.query.filter_by(id=temp).update(dict(id=idx))

		db.session.commit()

	else:
		print('publication == None || publication_next == None')

def publication_arrow_down(id):

	idx = int(id)
	idx_prev = idx-1
	temp = -1

	publication = models.Publications.query.filter_by(id=idx).first()
	publication_prev = models.Publications.query.filter_by(id=idx_prev).first()

	if publication != None and publication_prev != None:
		models.Publications.query.filter_by(id=idx_prev).update(dict(id=temp))
		models.Publications.query.filter_by(id=idx).update(dict(id=idx_prev))
		models.Publications.query.filter_by(id=temp).update(dict(id=idx))

		db.session.commit()

	else:
		print('publication == None || publication_prev == None')

def publication_toggle_show(id):

	idx = int(id)
	item = models.Publications.query.filter_by(id=idx).first()

	print(item.show)

	if item != None:
		models.Publications.query.filter_by(id=idx).update(dict(show = (item.show == False)))
		db.session.commit()
	else:
		print('item == None')