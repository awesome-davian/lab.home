import os
from app import app, db, models
# from werkzeug.utils import secure_filename
from datetime import datetime
from sqlalchemy import desc

logger = app.logger

def get_table(category) :
	if category == 'news':
		return models.News
	elif category == 'people':
		return models.Member
	elif category == 'publications':
		return models.Publications
	elif category == 'research':
		return models.Research
	elif category == 'teaching':
		return models.Teaching
	elif category == 'links':
		return models.Links
	else:
		return None

def update_lab_info(desc, sub_desc, bg_filename, bg_image):

	if bg_image != None:
		# bg_name = secure_filename(bg_image.filename)
		bg_name = bg_image.filename
		
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

	max_sn = 0
	if models.News.query.count() != 0:
		max_sn = models.News.query.order_by(desc(models.News.sn)).first().sn

	news = models.News(sn=max_sn+1, title=title, contents=contents, date=date_python, show=show)

	print(news)
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

def insert_research(title, text1, text2, teaser_image_path, member, publications, is_activated, show):

	max_sn = 0
	if models.Research.query.count() != 0:
		max_sn = models.Research.query.order_by(desc(models.Research.sn)).first().sn

	research = models.Research(sn=max_sn+1, title=title, text1=text1, text2=text2, teaser_image_path=teaser_image_path, member=member, publications=publications, is_activated=is_activated, show=show)
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

def insert_member(name, email, student_id, course, picture, interest, bs, ms, introduction, link_github, link_facebook, link_twitter, link_linkedin, show):

	if picture != None:
		print(picture.filename)
		# picture_name = "%s_%s" % (name, secure_filename(picture.filename))
		picture_name = "%s_%s" % (name, picture.filename)
		print(picture_name)

		picture_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/member/')
		picture_path = os.path.join(picture_path, picture_name)
		
		print(picture_path)
		picture.save(picture_path)
	else:
		picture_name = ''

	max_sn = 0
	if models.Member.query.count() != 0:
		max_sn = models.Member.query.order_by(desc(models.Member.sn)).first().sn
	
	member = models.Member(sn=max_sn+1, name=name, email=email, student_id=student_id, course=course, picture_path=picture_name, interest=interest, bs=bs, ms=ms, introduction=introduction, link_github=link_github, link_facebook=link_facebook, link_twitter=link_twitter, link_linkedin=link_linkedin, show=show)
	db.session.add(member)
	db.session.commit()

def update_member(id, name, email, student_id, course, picture_filename, picture, interest, bs, ms, introduction, link_homepage, link_github, link_facebook, link_twitter, link_linkedin, show):

	if picture != None:
		print(picture.filename)
		# picture_name = "%s_%s" % (name, secure_filename(picture.filename))
		picture_name = "%s_%s" % (name, picture.filename)
		print(picture_name)

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
		member.update(dict(link_homepage=link_homepage))
		member.update(dict(link_github=link_github))
		member.update(dict(link_facebook=link_facebook))
		member.update(dict(link_twitter=link_twitter))
		member.update(dict(link_linkedin=link_linkedin))
		member.update(dict(show=show))

		db.session.commit()
	else:
		print('member == None')

def insert_teaching(code, name, description, when, target_audience, link, video, show):

	max_sn = 0
	if models.Teaching.query.count() != 0:
		max_sn = models.Teaching.query.order_by(desc(models.Teaching.sn)).first().sn

	teaching = models.Teaching(sn=max_sn+1, code=code, name=name, description=description, when=when, target_audience=target_audience, link=link, video=video, show=show)
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

def insert_publication(title, description, year, abstract, teaser_image, authors, link_pdf1, link_video, link_source, link_url, show):

	if teaser_image != None:
		# teaser_image_name = secure_filename(teaser_image.filename)
		teaser_image_name = teaser_image.filename

		teaser_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/publications/')
		teaser_path = os.path.join(teaser_path, teaser_image_name)
		
		print(teaser_path)
		teaser_image.save(teaser_path)
	else:
		teaser_image_name = ''

	max_sn = 0
	if models.Publications.query.count() != 0:
		max_sn = models.Publications.query.order_by(desc(models.Publications.sn)).first().sn
	
	publications = models.Publications(sn=max_sn+1, title=title, description=description, year=year, abstract=abstract, teaser_image_path=teaser_image_name, authors=authors, link_pdf1=link_pdf1, link_video=link_video, link_source=link_source, link_url=link_url, show=show)
	db.session.add(publications)
	db.session.commit()

# def update_publication(id, title, description, abstract, teaser_image_path, authors, link_pdf1, link_pdf2, link_video, link_source, link_url, link_etc):
def update_publication(id, title, description, year, abstract, teaser_filename, teaser_image, authors, link_pdf1, link_video, link_source, link_url, show):

	
	if teaser_image != None:
		# teaser_image_name = secure_filename(teaser_image.filename)
		teaser_image_name = teaser_image.filename

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

def insert_link(name, description, image_path, link_url, link_etc, show):

	
	if image_path != None:
		# imagefile_name = secure_filename(image_path.filename)
		imagefile_name = image_path.filename

		image_full_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/links/')
		image_full_path = os.path.join(image_full_path, imagefile_name)
		
		print(image_full_path)
		image_path.save(image_full_path)

	max_sn = 0
	if models.Links.query.count() != 0:
		max_sn = models.Links.query.order_by(desc(models.Links.sn)).first().sn
	

	links = models.Links(sn=max_sn+1, name=name, description=description, image_path=imagefile_name, link_url=link_url, link_etc=link_etc, show=show)
	db.session.add(links)
	db.session.commit()

def update_link(id, name, description, image_name, image_path, link_url, link_etc, show):

	
	if image_path != None:
		# imagefile_name = secure_filename(image_path.filename)
		imagefile_name = image_path.filename

		image_full_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/links/')
		image_full_path = os.path.join(image_full_path, imagefile_name)
		
		print(image_full_path)
		image_path.save(image_full_path)
	else:
		if image_name != '':
			imagefile_name = image_name
		else:
			imagefile_name = ''

	links = models.Links.query.filter_by(id=int(id))
	
	if links != None:
		print('links != None')
		links.update(dict(name=name))
		links.update(dict(description=description))
		links.update(dict(image_path=imagefile_name))
		links.update(dict(link_url=link_url))
		links.update(dict(link_etc=link_etc))
		links.update(dict(show=show))
		
		db.session.commit()
	else:
		print('links == None')

def delete_item(category, id):

	table = get_table(category)

	item = table.query.filter_by(id=int(id)).first()
	if item != None:
		db.session.delete(item)
		db.session.commit()
	else:
		print('item == None')

def toggle_show(category, id):

	table = get_table(category)

	idx = int(id)
	item = table.query.filter_by(id=idx).first()

	print(item.show)

	if item != None:
		table.query.filter_by(id=idx).update(dict(show = (item.show == False)))
		db.session.commit()
	else:
		print('item == None')

def change_position(category, sn, direction):

	print('change_position({}, {}, {})'.format(category, sn, direction))

	table = get_table(category)

	sn = int(sn)

	item = table.query.filter_by(sn=sn).first()
	
	# item_next = table.query.filter_by(sn=sn_next).first()
	if direction == 'up':
		temp_item = table.query.filter(table.sn>sn).order_by(table.sn)	
	else:
		temp_item = table.query.filter(table.sn<sn).order_by(desc(table.sn))
	
	item_next = temp_item.first()
	sn_next =item_next.sn

	temp = -1
	if item != None and item_next != None:
		table.query.filter_by(sn=sn_next).update(dict(sn=temp))
		table.query.filter_by(sn=sn).update(dict(sn=sn_next))
		table.query.filter_by(sn=temp).update(dict(sn=sn))

		db.session.commit()

	else:
		print('change position failed')