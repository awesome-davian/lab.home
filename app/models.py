# coding: utf-8
from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
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
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	description = db.Column(db.String(128), index=True, unique=True)
	sub_description = db.Column(db.String(128), index=True, unique=True)
	background_img_path = db.Column(db.String(128), index=True, unique=True)

	def __repr__(self):
		return '<LabInfo %r>' % (self.name)

class About(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(64), index=True, unique=True)
	sub_text = db.Column(db.String(128), index=True, unique=True)

	def __repr__(self):
		return '<About %r>' % (self.text)

class News(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), index=True, unique=True)
	contents = db.Column(db.String(128), index=True, unique=True)
	date = db.Column(db.DateTime, index=True, unique=True)

	def __repr__(self):
		return '<News %r>' % (self.title)

class Research(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), index=True, unique=True)
	text1 = db.Column(db.String(128), index=True, unique=True)
	text2 = db.Column(db.String(128), index=True, unique=True)
	teaser_image_path = db.Column(db.String(128), index=True, unique=True)
	member = db.Column(db.String(64), index=True, unique=True)
	publications = db.Column(db.String(64), index=True, unique=True)
	is_activated = db.Column(db.Boolean, index=True, unique=True)

	def __repr__(self):
		return '<Research %r>' % (self.title)

class Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	student_id = db.Column(db.String(128), index=True, unique=True)
	course = db.Column(db.String(128), index=True, unique=True)
	picture_path = db.Column(db.String(64), index=True, unique=True)	
	introduction = db.Column(db.String(64), index=True, unique=True)
	bd = db.Column(db.String(64), index=True, unique=True)
	md = db.Column(db.String(64), index=True, unique=True)
	career1 = db.Column(db.String(64), index=True, unique=True)
	career2 = db.Column(db.String(64), index=True, unique=True)
	career3 = db.Column(db.String(64), index=True, unique=True)
	link_github = db.Column(db.String(64), index=True, unique=True)
	link_facebook = db.Column(db.String(64), index=True, unique=True)
	link_twitter = db.Column(db.String(64), index=True, unique=True)
	link_linkedin = db.Column(db.String(64), index=True, unique=True)
	link1 = db.Column(db.String(64), index=True, unique=True)
	link2 = db.Column(db.String(64), index=True, unique=True)
	link3 = db.Column(db.String(64), index=True, unique=True)
	link4 = db.Column(db.String(64), index=True, unique=True)

	def __repr__(self):
		return '<Member %r>' % (self.name)

class Teaching(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(64), index=True, unique=True)
	name = db.Column(db.String(128), index=True, unique=True)
	description = db.Column(db.String(128), index=True, unique=True)
	when = db.Column(db.String(128), index=True, unique=True)
	target_audience = db.Column(db.String(64), index=True, unique=True)
	link1 = db.Column(db.String(64), index=True, unique=True)
	link2 = db.Column(db.String(64), index=True, unique=True)

	def __repr__(self):
		return '<Teaching %r>' % (self.name)

class Publications(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), index=True, unique=True)
	conference = db.Column(db.String(128), index=True, unique=True)
	abstract = db.Column(db.String(128), index=True, unique=True)
	date = db.Column(db.String(128), index=True, unique=True)
	teaser_image_path = db.Column(db.String(128), index=True, unique=True)
	authors = db.Column(db.String(64), index=True, unique=True)
	link_pdf1 = db.Column(db.String(64), index=True, unique=True)
	link_pdf2 = db.Column(db.String(64), index=True, unique=True)
	link_video = db.Column(db.String(64), index=True, unique=True)
	link_source = db.Column(db.String(64), index=True, unique=True)
	link_url = db.Column(db.String(64), index=True, unique=True)
	link_etc = db.Column(db.String(64), index=True, unique=True)

	def __repr__(self):
		return '<Publications %r>' % (self.title)