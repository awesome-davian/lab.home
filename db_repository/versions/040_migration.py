from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
member = Table('member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('sn', Integer),
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
    Column('link_homepage', String(length=512)),
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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['member'].columns['link_homepage'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['member'].columns['link_homepage'].drop()
