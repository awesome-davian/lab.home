from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
member = Table('member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('name_ko', String(length=64)),
    Column('email', String(length=128)),
    Column('student_id', String(length=128)),
    Column('course', Integer),
    Column('picture_path', String(length=512)),
    Column('interest', String(length=1024)),
    Column('bs', String(length=128)),
    Column('ms', String(length=128)),
    Column('introduction', String(length=1024)),
    Column('career1', String(length=128)),
    Column('career2', String(length=128)),
    Column('career3', String(length=128)),
    Column('link_github', String(length=512)),
    Column('link_facebook', String(length=512)),
    Column('link_twitter', String(length=512)),
    Column('link_linkedin', String(length=512)),
    Column('link1', String(length=512)),
    Column('link2', String(length=512)),
    Column('link3', String(length=512)),
    Column('link4', String(length=512)),
    Column('show', Boolean),
)

research = Table('research', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=128)),
    Column('title_ko', String(length=128)),
    Column('text1', String(length=1024)),
    Column('text1_ko', String(length=1024)),
    Column('text2', String(length=1024)),
    Column('text2_ko', String(length=1024)),
    Column('teaser_image_path', String(length=512)),
    Column('member', String(length=1024)),
    Column('publications', String(length=1024)),
    Column('is_activated', Boolean),
    Column('show', Boolean),
)

news = Table('news', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=128)),
    Column('contents', String(length=1024)),
    Column('date', DateTime),
    Column('show', Boolean),
)

publications = Table('publications', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=128)),
    Column('description', String(length=4096)),
    Column('abstract', String(length=1024)),
    Column('year', Integer),
    Column('teaser_image_path', String(length=512)),
    Column('authors', String(length=1024)),
    Column('link_pdf1', String(length=512)),
    Column('link_pdf2', String(length=512)),
    Column('link_video', String(length=512)),
    Column('link_source', String(length=512)),
    Column('link_url', String(length=512)),
    Column('link_etc', String(length=512)),
    Column('is_activated', Boolean),
    Column('show', Boolean),
)

teaching = Table('teaching', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('code', String(length=128)),
    Column('name', String(length=128)),
    Column('name_ko', String(length=128)),
    Column('description', String(length=1024)),
    Column('description_ko', String(length=1024)),
    Column('when', String(length=128)),
    Column('target_audience', String(length=128)),
    Column('link', String(length=512)),
    Column('video', String(length=512)),
    Column('show', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['member'].columns['show'].create()
    post_meta.tables['research'].columns['show'].create()
    post_meta.tables['news'].columns['show'].create()
    post_meta.tables['publications'].columns['show'].create()
    post_meta.tables['teaching'].columns['show'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['member'].columns['show'].drop()
    post_meta.tables['research'].columns['show'].drop()
    post_meta.tables['news'].columns['show'].drop()
    post_meta.tables['publications'].columns['show'].drop()
    post_meta.tables['teaching'].columns['show'].drop()
