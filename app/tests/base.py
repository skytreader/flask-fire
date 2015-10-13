from flask.ext.testing import TestCase
from app.models import get_or_create, User
import app
import logging
import unittest

app.app.config["TESTING"] = True
app.init_db(app.app.config["SQLALCHEMY_TEST_DATABASE_URI"])
app.init_blueprints()

class AppTestCase(TestCase):
    
    def create_app(self):
        return app.app
    
    def setUp(self):
        self.admin_user = get_or_create(User, will_commit = True, username="admin",
          password="admin", can_read=True, can_write=True, can_exec=True)
        app.db.session.flush()

    def verify_inserted(self, model, **kwargs):
        """
        Verify that the record described by **kwargs is inserted into the table
        represented by the given model. Returns the inserted record (if the
        assert succeeds.
        """
        record = app.db.session.query(model).filter_by(**kwargs).first()
        self.assertTrue(record is not None)
        return record

    def verify_does_not_exist(self, model, **kwargs):
        """
        Verify that the record described by **kwargs is not yet in the table
        represented by the given model.
        """
        record = app.db.session.query(model).filter_by(**kwargs).first()
        self.assertTrue(record is None)

    def tearDown(self):
        """
        Rollback any pending transactions and delete the contents of the tables.

        This is done directly on DB level. Note that the "proper" SQLAlchemy
        way to do this would be https://bitbucket.org/zzzeek/sqlalchemy/wiki/UsageRecipes/DropEverything
        but it is unsuitable for unit testing since we drop _everything_.

        (Or it _might_ work but we will have to call `create_all` on setUp which
        is going to be a waste of time.)
        """
        app.db.session.rollback()
        app.db.engine.execute("SET FOREIGN_KEY_CHECKS = 0;")
        app.db.engine.execute("SET FOREIGN_KEY_CHECKS = 1;")
        app.db.session.commit()
