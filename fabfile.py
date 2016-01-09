from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TEST_DATABASE_URI
from fabric.api import local
from fixtures import insert_fixtures
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
Update this file as you add database tables.
"""

def reset_db_data():
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    session = sessionmaker(bind=engine)()
    engine.execute("SET FOREIGN_KEY_CHECKS = 0;")
    engine.execute("TRUNCATE alembic_version;")
    engine.execute("TRUNCATE users;")
    engine.execute("SET FOREIGN_KEY_CHECKS = 1;")
    session.commit()

    insert_fixtures(engine, session)

def destroy_db_tables():
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    session = sessionmaker(bind=engine)()
    engine.execute("SET FOREIGN_KEY_CHECKS = 0;")
    engine.execute("DROP TABLE IF EXISTS alembic_version;")
    engine.execute("DROP TABLE IF EXISTS users;")
    engine.execute("SET FOREIGN_KEY_CHECKS = 1;")
    session.commit()

def manual_test_cleanup():
    engine = create_engine(SQLALCHEMY_TEST_DATABASE_URI)
    session = sessionmaker(bind=engine)()
    engine.execute("SET FOREIGN_KEY_CHECKS = 0;")
    engine.execute("DELETE FROM alembic_version;")
    engine.execute("DELETE FROM users;")
    engine.execute("SET FOREIGN_KEY_CHECKS = 1;")
    session.commit()

def dbdump():
    local("mysqldump -u root app > app.sql")

def destroy_database(is_test=False):
    if is_test:
        local('mysql -u root -e "DROP DATABASE app_test"')
    else:
        local('mysql -u root -e "DROP DATABASE app"')

def create_database(is_test=False):
    if is_test: 
        local('mysql -u root -e "CREATE DATABASE app_test DEFAULT CHARACTER SET = utf8"')
    else:
        local('mysql -u root -e "CREATE DATABASE app DEFAULT CHARACTER SET = utf8"')
