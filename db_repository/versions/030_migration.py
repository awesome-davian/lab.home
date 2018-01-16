from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
lab_info = Table('lab_info', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('description', VARCHAR(length=1024)),
    Column('description_ko', VARCHAR(length=128)),
    Column('sub_description', VARCHAR(length=128)),
    Column('sub_description_ko', VARCHAR(length=128)),
    Column('background_img_path', VARCHAR(length=128)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['lab_info'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['lab_info'].create()
