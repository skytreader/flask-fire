from base import AppTestCase
from faker import Faker
from flask.ext.login import login_user

import factory
import flask.ext.login
import json
import app
import re
import string
import unittest

fake = Faker()

class ApiTests(AppTestCase):
    
    def setUp(self):
        super(ApiTests, self).setUp()
