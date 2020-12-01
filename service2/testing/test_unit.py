from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class Testd20(TestBase):
    def test_d20(self):
            response = self.client.get('/d20')
            self.assertIs(type(response.data.decode('utf-8')),int)
        
