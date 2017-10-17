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



# class Publications(Document):
#     __database__ = 'davian_web'
#     __collection__ = 'Publication'

#     structure = {
#         'title': unicode,
#         'authors': list,         # 우리 연구실에 없는 사람인 경우 어떻게 하지?!
#         'conference': unicode,
#         'year': unicode,           # format : 'yyyy-mm'
#         'status': unicode,          # accept or not
#         'abstract': unicode,
#         # 학회, 연도, 상태, abstract

#         # file address
#         'image': unicode,
#         'pdf': unicode,
#         'video': unicode
#     }

#     required_fields = ['title', 'authors', 'conference', 'year', 'status']
#     default_value = {'image': '', 'pdf': '', 'video': '', 'abstract': ''}
#     use_dot_notation = True


# class Links(Document):
#     __database__ = 'davian_web'
#     __collection__ = 'Link'

#     structure = {
#         'url': unicode,
#         'description': unicode,
#         'category': unicode,
#         'created': datetime
#     }

#     required_fields = ['url', 'description', 'category']
#     default_values = {'created': datetime.utcnow}
#     use_dot_notation = True
