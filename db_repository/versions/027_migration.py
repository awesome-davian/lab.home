from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
about = Table('about', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('text', String(length=64)),
    Column('text_ko', String(length=64)),
    Column('sub_text', String(length=128)),
    Column('sub_text_ko', String(length=128)),
)

member = Table('member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('name_ko', String(length=64)),
    Column('email', String(length=128)),
    Column('student_id', String(length=128)),
    Column('course', Integer),
    Column('picture_path', String(length=64)),
    Column('interest', String(length=64)),
    Column('bs', String(length=64)),
    Column('ms', String(length=64)),
    Column('introduction', String(length=64)),
    Column('career1', String(length=64)),
    Column('career2', String(length=64)),
    Column('career3', String(length=64)),
    Column('link_github', String(length=64)),
    Column('link_facebook', String(length=64)),
    Column('link_twitter', String(length=64)),
    Column('link_linkedin', String(length=64)),
    Column('link1', String(length=64)),
    Column('link2', String(length=64)),
    Column('link3', String(length=64)),
    Column('link4', String(length=64)),
)

news = Table('news', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('contents', String(length=128)),
    Column('date', DateTime),
)

publications = Table('publications', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('description', String(length=128)),
    Column('abstract', String(length=128)),
    Column('year', Integer),
    Column('teaser_image_path', String(length=128)),
    Column('authors', String(length=64)),
    Column('link_pdf1', String(length=64)),
    Column('link_pdf2', String(length=64)),
    Column('link_video', String(length=64)),
    Column('link_source', String(length=64)),
    Column('link_url', String(length=64)),
    Column('link_etc', String(length=64)),
    Column('is_activated', Boolean),
)

research = Table('research', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('title_ko', String(length=64)),
    Column('text1', String(length=128)),
    Column('text1_ko', String(length=128)),
    Column('text2', String(length=128)),
    Column('text2_ko', String(length=128)),
    Column('teaser_image_path', String(length=128)),
    Column('member', String(length=64)),
    Column('publications', String(length=64)),
    Column('is_activated', Boolean),
)

teaching = Table('teaching', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('code', String(length=64)),
    Column('name', String(length=128)),
    Column('name_ko', String(length=128)),
    Column('description', String(length=128)),
    Column('description_ko', String(length=128)),
    Column('when', String(length=128)),
    Column('target_audience', String(length=64)),
    Column('link', String(length=64)),
    Column('video', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['about'].create()
    post_meta.tables['member'].create()
    post_meta.tables['news'].create()
    post_meta.tables['publications'].create()
    post_meta.tables['research'].create()
    post_meta.tables['teaching'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['about'].drop()
    post_meta.tables['member'].drop()
    post_meta.tables['news'].drop()
    post_meta.tables['publications'].drop()
    post_meta.tables['research'].drop()
    post_meta.tables['teaching'].drop()
