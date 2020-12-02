from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class Testd20(TestBase):
    def test_d20(self):
        response = self.client.get('/d20')
        d20=response.data.decode('utf-8').isnumeric() and int(response.data.decode('utf-8'))>=1 and int(response.data.decode('utf-8'))<=20
        self.assertTrue(d20)

        
