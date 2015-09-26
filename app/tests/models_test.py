from base import AppTestCase
from factories import *
from app.models import get_or_create

import app
import unittest

class ModelsTest(AppTestCase):
    
    def setUp(self):
        super(ModelsTest, self).setUp()

    def test_get_or_create_commit(self):
        # TODO
        pass

    def test_get_or_create_nocommit(self):
        # TODO
        pass

    def test_get_or_create_preexisting(self):
        # TODO
        pass
    
    def test_get_or_create_insuff(self):
        # TODO
        pass
