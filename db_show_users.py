from app import db, models

users = models.User.query.all()

for u in users:
	print(u.id, u.nickname, u.email)