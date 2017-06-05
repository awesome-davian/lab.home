from app import db, models

u = models.User(nickname='mchoi', email='mchoi@gmail.com')
db.session.add(u)
db.session.commit()