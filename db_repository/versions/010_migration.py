from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
migration_tmp = Table('migration_tmp', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=64)),
    Column('text1', VARCHAR(length=128)),
    Column('text2', VARCHAR(length=128)),
    Column('teaser_image_path', VARCHAR(length=128)),
    Column('member', VARCHAR(length=64)),
    Column('publications', VARCHAR(length=64)),
    Column('in_activate', BOOLEAN),
)

research = Table('research', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('text1', String(length=128)),
    Column('text2', String(length=128)),
    Column('teaser_image_path', String(length=128)),
    Column('member', String(length=64)),
    Column('publications', String(length=64)),
    Column('is_activated', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].drop()
    post_meta.tables['research'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].create()
    post_meta.tables['research'].drop()
