from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
links = Table('links', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('sn', Integer),
    Column('name', String(length=128)),
    Column('description', String(length=4096)),
    Column('image_path', String(length=512)),
    Column('link_url', String(length=512)),
    Column('link_etc', String(length=512)),
    Column('is_activated', Boolean),
    Column('show', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['links'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['links'].drop()
