# coding: utf-8
from datetime import datetime
import flask_login


class User(flask_login.UserMixin):
    pass



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
