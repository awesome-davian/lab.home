# from pymongo import MongoClient

# WTF_CSRF_ENABLED = True
# SECRET_KEY = '12345678'
# DB_NAME = 'homepage'

# DATABASE = MongoClient()[DB_NAME]
# #POSTS_COLLECTION = DATABASE.posts
# USERS_COLLECTION = DATABASE.users
# #SETTINGS_COLLECTION = DATABASE.settings

# DEBUG = True

import os
basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(basedir, 'app/static/src/')