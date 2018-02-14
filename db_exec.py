from app import db, models

#-------------------------------------------------------------------
#- print information of all tables
#-------------------------------------------------------------------
# users = models.User.query.all()

# for user in users:
# 	print('%d, %s, %s' % (user.id, user.nickname, user.email))

# labinfo = models.LabInfo.query.all()
# for info in labinfo:
# 	print('%d, %s, %s, %s' % (info.id, info.name, info.description, info.sub_description))

#-------------------------------------------------------------------
#- print user information
#-------------------------------------------------------------------
# users = models.User.query.all()

# for user in users:
# 	print('%d, %s, %s' % (user.id, user.nickname, user.email))

#-------------------------------------------------------------------
#- insert a Lab. information
#-------------------------------------------------------------------
# u = models.LabInfo(name='DAVIAN', description='Data and Visual Analytics Lab.', sub_description='^^')
# db.session.add(u)
# db.session.commit()

#-------------------------------------------------------------------
#- display a Lab. information
#-------------------------------------------------------------------
# info = models.LabInfo.query.filter_by(id = 1).first()
# if info == None:
# 	print('None')
# else:
# 	print(info.id)
# 	print(info.name)
# 	print(info.description)
# 	print(info.sub_description)
# 	print(info.background_img_path)

# info = models.LabInfo.query.filter_by(id = 1).update(dict(description='Data and Visual Analytics Lab.'))
# db.session.commit()

#-------------------------------------------------------------------
#- insert a About information
#-------------------------------------------------------------------
# u = models.About(text='text', sub_text='sub_text')
# db.session.add(u)
# db.session.commit()

#-------------------------------------------------------------------
#- display a About information
#-------------------------------------------------------------------
# info = models.About.query.filter_by(id = 1).first()
# if info == None:
# 	print('None')
# else:
# 	print(info.text)
# 	print(info.sub_text)

# info = models.LabInfo.query.filter_by(id = 1).update(dict(description='Data and Visual Analytics Lab.'))
# db.session.commit()

#-------------------------------------------------------------------
#- ID modification
#-------------------------------------------------------------------
# info = models.News.query.filter_by(id=-1).update(dict(id=10))
# db.session.commit()

#-------------------------------------------------------------------
#- Remove All items
#-------------------------------------------------------------------
# models.About.query.delete()

# meta = db.metadata
# for table in reversed(meta.sorted_tables):
# 	if table.name != 'user' and table.name != 'post' and table.name != 'lab_info':
# 		print('Clear table %s' % table.name)
# 		db.session.execute(table.delete())
# 		# db.session.execute(table.drop(db.engine))

# db.session.commit()
# db.session.close()

#-------------------------------------------------------------------
#- Delete database
#-------------------------------------------------------------------
# db.reflect()
# db.drop_all()
# db.session.close()

#-------------------------------------------------------------------
#- Drop table
#-------------------------------------------------------------------
# models.Links.__table__.drop(db.engine) --> this works

#-------------------------------------------------------------------
#- Show table attributes
#-------------------------------------------------------------------
# info = models.Links.__table__.columns._data
# info = models.Links.__mapper__.columns.keys()

# print(info)
# for item in info:
# 	print('%r' % item)
	 # if item in values:
	 	# yield item, values[attr]

#-------------------------------------------------------------------
#- Modifing the data
#-------------------------------------------------------------------
model = models.Publications.query.all()
count = len(model)
for i in range(1, count+1):
	item = models.Publications.query.filter_by(id=i).update(dict(thumbnail_image_path=''))
	db.session.commit()