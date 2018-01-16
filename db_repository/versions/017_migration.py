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
    Column('bs', VARCHAR(length=64)),
    Column('ms', VARCHAR(length=64)),
    Column('introduction', VARCHAR(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['member'].columns['course'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['member'].columns['course'].create()
