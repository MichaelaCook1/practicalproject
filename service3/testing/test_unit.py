from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class Testd12(TestBase):
    def test_d12(self):
        response = self.client.get('/d12')
        d12=response.data.decode('utf-8').isnumeric() and int(response.data.decode('utf-8'))>=1 and int(response.data.decode('utf-8'))<=12
        self.assertTrue(d12)
~                                                          
