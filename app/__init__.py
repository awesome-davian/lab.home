# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging import FileHandler, WARNING, INFO, DEBUG
from app import gpuinfo_bp

app = Flask(__name__)

file_handler = FileHandler('/tmp/davian.log')
file_handler.setLevel(DEBUG)

app.config.from_object('config')
app.logger.addHandler(file_handler)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

app.register_blueprint(gpuinfo_bp.gpuinfo)

from app import views, models