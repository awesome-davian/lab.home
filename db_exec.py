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
info = models.About.query.filter_by(id = 1).first()
if info == None:
	print('None')
else:
	print(info.text)
	print(info.sub_text)

# info = models.LabInfo.query.filter_by(id = 1).update(dict(description='Data and Visual Analytics Lab.'))
# db.session.commit()