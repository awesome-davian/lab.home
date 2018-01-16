from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
member = Table('member', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('email', VARCHAR(length=128)),
    Column('student_id', VARCHAR(length=128)),
    Column('course', VARCHAR(length=128)),
    Column('picture_path', VARCHAR(length=64)),
    Column('bd', VARCHAR(length=64)),
    Column('md', VARCHAR(length=64)),
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
    Column('interest', VARCHAR(length=64)),
)

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
    pre_meta.tables['member'].columns['bd'].drop()
    pre_meta.tables['member'].columns['md'].drop()
    post_meta.tables['member'].columns['bs'].create()
    post_meta.tables['member'].columns['ms'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['member'].columns['bd'].create()
    pre_meta.tables['member'].columns['md'].create()
    post_meta.tables['member'].columns['bs'].drop()
    post_meta.tables['member'].columns['ms'].drop()
