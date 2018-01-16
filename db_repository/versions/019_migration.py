from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
teaching = Table('teaching', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('code', VARCHAR(length=64)),
    Column('name', VARCHAR(length=128)),
    Column('description', VARCHAR(length=128)),
    Column('when', VARCHAR(length=128)),
    Column('target_audience', VARCHAR(length=64)),
    Column('link1', VARCHAR(length=64)),
    Column('link2', VARCHAR(length=64)),
)

teaching = Table('teaching', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('code', String(length=64)),
    Column('name', String(length=128)),
    Column('description', String(length=128)),
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
    pre_meta.tables['teaching'].columns['link1'].drop()
    pre_meta.tables['teaching'].columns['link2'].drop()
    post_meta.tables['teaching'].columns['link'].create()
    post_meta.tables['teaching'].columns['video'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['teaching'].columns['link1'].create()
    pre_meta.tables['teaching'].columns['link2'].create()
    post_meta.tables['teaching'].columns['link'].drop()
    post_meta.tables['teaching'].columns['video'].drop()
