# coding: utf-8
from datetime import datetime
# from flask_mongokit import Document

from werkzeug.security import check_password_hash


class User():

    def __init__(self, email):
        self.email = None

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def login(self):
        return True

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)



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
