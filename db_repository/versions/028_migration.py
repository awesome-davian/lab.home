from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
about = Table('about', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('text', VARCHAR(length=64)),
    Column('text_ko', VARCHAR(length=64)),
    Column('sub_text', VARCHAR(length=128)),
    Column('sub_text_ko', VARCHAR(length=128)),
)

lab_info = Table('lab_info', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('description', VARCHAR(length=128)),
    Column('sub_description', VARCHAR(length=128)),
    Column('background_img_path', VARCHAR(length=128)),
    Column('description_ko', VARCHAR(length=128)),
    Column('sub_description_ko', VARCHAR(length=128)),
)

member = Table('member', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('name_ko', VARCHAR(length=64)),
    Column('email', VARCHAR(length=128)),
    Column('student_id', VARCHAR(length=128)),
    Column('course', INTEGER),
    Column('picture_path', VARCHAR(length=64)),
    Column('interest', VARCHAR(length=64)),
    Column('bs', VARCHAR(length=64)),
    Column('ms', VARCHAR(length=64)),
    Column('introduction', VARCHAR(length=64)),
    Column('career1', VARCHAR(length=64)),
    Column('career2', VARCHAR(length=64)),
    Column('career3', VARCHAR(length=64)),
    Column('link_github', VARCHAR(length=64)),
    Column('link_facebook', VARCHAR(length=64)),
    Column('link_twitter', VARCHAR(length=64)),
    Column('link_linkedin', VARCHAR(length=64)),
    Column('link1', VARCHAR(length=64)),
    Column('link2', VARCHAR(length=64)),
    Column('link3', VARCHAR(length=64)),
    Column('link4', VARCHAR(length=64)),
)

news = Table('news', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=64)),
    Column('contents', VARCHAR(length=128)),
    Column('date', DATETIME),
)

publications = Table('publications', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=64)),
    Column('description', VARCHAR(length=128)),
    Column('abstract', VARCHAR(length=128)),
    Column('year', INTEGER),
    Column('teaser_image_path', VARCHAR(length=128)),
    Column('authors', VARCHAR(length=64)),
    Column('link_pdf1', VARCHAR(length=64)),
    Column('link_pdf2', VARCHAR(length=64)),
    Column('link_video', VARCHAR(length=64)),
    Column('link_source', VARCHAR(length=64)),
    Column('link_url', VARCHAR(length=64)),
    Column('link_etc', VARCHAR(length=64)),
    Column('is_activated', BOOLEAN),
)

research = Table('research', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=64)),
    Column('title_ko', VARCHAR(length=64)),
    Column('text1', VARCHAR(length=128)),
    Column('text1_ko', VARCHAR(length=128)),
    Column('text2', VARCHAR(length=128)),
    Column('text2_ko', VARCHAR(length=128)),
    Column('teaser_image_path', VARCHAR(length=128)),
    Column('member', VARCHAR(length=64)),
    Column('publications', VARCHAR(length=64)),
    Column('is_activated', BOOLEAN),
)

teaching = Table('teaching', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('code', VARCHAR(length=64)),
    Column('name', VARCHAR(length=128)),
    Column('name_ko', VARCHAR(length=128)),
    Column('description', VARCHAR(length=128)),
    Column('description_ko', VARCHAR(length=128)),
    Column('when', VARCHAR(length=128)),
    Column('target_audience', VARCHAR(length=64)),
    Column('link', VARCHAR(length=64)),
    Column('video', VARCHAR(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['about'].drop()
    pre_meta.tables['lab_info'].drop()
    pre_meta.tables['member'].drop()
    pre_meta.tables['news'].drop()
    pre_meta.tables['publications'].drop()
    pre_meta.tables['research'].drop()
    pre_meta.tables['teaching'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['about'].create()
    pre_meta.tables['lab_info'].create()
    pre_meta.tables['member'].create()
    pre_meta.tables['news'].create()
    pre_meta.tables['publications'].create()
    pre_meta.tables['research'].create()
    pre_meta.tables['teaching'].create()
