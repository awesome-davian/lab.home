# coding: utf-8
from app import db

LEN_NAME = 64
LEN_EMAIL = 128
LEN_TITLE = 128
LEN_LINK = 512
LEN_PATH = 512
LEN_SHORT_TEXT = 128
LEN_TEXT = 1024
LEN_LONG_TEXT = 4096

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)	
	nickname = db.Column(db.String(64), index=True)
	email = db.Column(db.String(120), index=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User %r>' % (self.nickname)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post %r>' % (self.body)

class LabInfo(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	sn = db.Column(db.Integer, index=True, unique=True, autoincrement=True)
	name = db.Column(db.String(LEN_NAME), index=True)
	description = db.Column(db.String(LEN_TEXT), index=True)
	description_ko = db.Column(db.String(LEN_TEXT), index=True)
	sub_description = db.Column(db.String(LEN_TEXT), index=True)
	sub_description_ko = db.Column(db.String(LEN_TEXT), index=True)
	background_img_path = db.Column(db.String(LEN_PATH), index=True)

	def __repr__(self):
		return '<LabInfo %r>' % (self.name)

class About(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sn = db.Column(db.Integer, unique=True)
	text = db.Column(db.String(LEN_TEXT), index=True)
	text_ko = db.Column(db.String(LEN_TEXT), index=True)
	sub_text = db.Column(db.String(LEN_TEXT), index=True)
	sub_text_ko = db.Column(db.String(LEN_TEXT), index=True)

	def __repr__(self):
		return '<About %r>' % (self.text)

class News(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sn = db.Column(db.Integer, unique=True)
	title = db.Column(db.String(LEN_TITLE), index=True)
	contents = db.Column(db.String(LEN_TEXT), index=True)
	date = db.Column(db.DateTime, index=True)
	show = db.Column(db.Boolean, index=True)

	def __repr__(self):
		return '<News %r, %r, %r, %r, %r>' % (self.sn, self.title, self.contents, self.date, self.show)

class Research(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sn = db.Column(db.Integer, unique=True)
	title = db.Column(db.String(LEN_TITLE), index=True)
	title_ko = db.Column(db.String(LEN_TITLE), index=True)
	text1 = db.Column(db.String(LEN_TEXT), index=True)
	text1_ko = db.Column(db.String(LEN_TEXT), index=True)
	text2 = db.Column(db.String(LEN_TEXT), index=True)
	text2_ko = db.Column(db.String(LEN_TEXT), index=True)
	teaser_image_path = db.Column(db.String(LEN_PATH), index=True)
	member = db.Column(db.String(LEN_TEXT), index=True)
	publications = db.Column(db.String(LEN_TEXT), index=True)
	is_activated = db.Column(db.Boolean, index=True)
	show = db.Column(db.Boolean, index=True)

	def __repr__(self):
		return '<Research %r>' % (self.title)

class Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sn = db.Column(db.Integer, unique=True)
	name = db.Column(db.String(LEN_NAME), index=True)
	name_ko = db.Column(db.String(LEN_NAME), index=True)
	email = db.Column(db.String(LEN_EMAIL), index=True, unique=True)
	student_id = db.Column(db.String(LEN_SHORT_TEXT), index=True, unique=True)
	course = db.Column(db.Integer, index=True)
	picture_path = db.Column(db.String(LEN_PATH), index=True)	
	interest = db.Column(db.String(LEN_TEXT), index=True)
	bs = db.Column(db.String(LEN_SHORT_TEXT), index=True)
	ms = db.Column(db.String(LEN_SHORT_TEXT), index=True)
	introduction = db.Column(db.String(LEN_TEXT), index=True)
	career1 = db.Column(db.String(LEN_SHORT_TEXT), index=True)
	career2 = db.Column(db.String(LEN_SHORT_TEXT), index=True)
	career3 = db.Column(db.String(LEN_SHORT_TEXT), index=True)
	link_homepage = db.Column(db.String(LEN_LINK), index=True)
	link_github = db.Column(db.String(LEN_LINK), index=True)
	link_facebook = db.Column(db.String(LEN_LINK), index=True)
	link_twitter = db.Column(db.String(LEN_LINK), index=True)
	link_linkedin = db.Column(db.String(LEN_LINK), index=True)
	link1 = db.Column(db.String(LEN_LINK), index=True)
	link2 = db.Column(db.String(LEN_LINK), index=True)
	link3 = db.Column(db.String(LEN_LINK), index=True)
	link4 = db.Column(db.String(LEN_LINK), index=True)
	show = db.Column(db.Boolean, index=True)

	def __repr__(self):
		return '<Member %r>' % (self.name)

class Teaching(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sn = db.Column(db.Integer, unique=True)
	code = db.Column(db.String(LEN_SHORT_TEXT), index=True)
	name = db.Column(db.String(LEN_TITLE), index=True)
	name_ko = db.Column(db.String(LEN_TITLE), index=True)
	description = db.Column(db.String(LEN_TEXT), index=True)
	description_ko = db.Column(db.String(LEN_TEXT), index=True)
	when = db.Column(db.String(LEN_SHORT_TEXT), index=True)
	target_audience = db.Column(db.String(LEN_SHORT_TEXT), index=True)
	link = db.Column(db.String(LEN_LINK), index=True)
	video = db.Column(db.String(LEN_LINK), index=True)
	show = db.Column(db.Boolean, index=True)

	def __repr__(self):
		return '<Teaching %r>' % (self.name)

class Publications(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sn = db.Column(db.Integer, unique=True)
	title = db.Column(db.String(LEN_TITLE), index=True)
	description = db.Column(db.String(LEN_LONG_TEXT), index=True)
	abstract = db.Column(db.String(LEN_TEXT), index=True)
	year = db.Column(db.Integer, index=True)
	teaser_image_path = db.Column(db.String(LEN_PATH), index=True)
	thumbnail_image_path = db.Column(db.String(LEN_PATH), index=True)
	authors = db.Column(db.String(LEN_TEXT), index=True)
	link_pdf1 = db.Column(db.String(LEN_LINK), index=True)
	link_pdf2 = db.Column(db.String(LEN_LINK), index=True)
	link_video = db.Column(db.String(LEN_LINK), index=True)
	link_source = db.Column(db.String(LEN_LINK), index=True)
	link_url = db.Column(db.String(LEN_LINK), index=True)
	link_etc = db.Column(db.String(LEN_LINK), index=True)
	is_activated = db.Column(db.Boolean, index=True)
	show = db.Column(db.Boolean, index=True)

	def __repr__(self):
		return '<Publications %r>' % (self.title)

class Links(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sn = db.Column(db.Integer, unique=True)
	name = db.Column(db.String(LEN_TITLE), index=True)
	description = db.Column(db.String(LEN_LONG_TEXT), index=True)
	image_path = db.Column(db.String(LEN_PATH), index=True)	
	link_url = db.Column(db.String(LEN_LINK), index=True)
	link_etc = db.Column(db.String(LEN_LINK), index=True)
	is_activated = db.Column(db.Boolean, index=True)
	show = db.Column(db.Boolean, index=True)

	def __repr__(self):
		return '<Links %r>' % (self.title)