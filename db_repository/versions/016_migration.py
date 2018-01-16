from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
member = Table('member', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('email', String(length=128)),
    Column('student_id', String(length=128)),
    Column('course', String(length=128)),
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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['member'].columns['introduction'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['member'].columns['introduction'].drop()
