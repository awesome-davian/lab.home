import os
from app import app, db, models
from werkzeug.utils import secure_filename

def update_lab_info(in_desc, in_sub_desc, in_bg_image):

	bg_name = secure_filename(in_bg_image.filename)

	if bg_name != '':
		
		bg_path = os.path.join(app.config['UPLOAD_FOLDER'],'img/')
		bg_path = os.path.join(bg_path, bg_name)
		
		print(bg_path)
		in_bg_image.save(bg_path)

	labinfo = models.LabInfo.query.filter_by(id = 1)
	if labinfo != None:
		labinfo.update(dict(description=in_desc))
		labinfo.update(dict(sub_description=in_sub_desc))
		if bg_name != '':
			labinfo.update(dict(background_img_path=bg_path))
		db.session.commit()
	else:
		print('labinfo == None')