from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
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
    post_meta.tables['teaching'].columns['description_ko'].create()
    post_meta.tables['teaching'].columns['name_ko'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['teaching'].columns['description_ko'].drop()
    post_meta.tables['teaching'].columns['name_ko'].drop()
