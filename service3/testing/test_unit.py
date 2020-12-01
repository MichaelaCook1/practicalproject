from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class Testd12(TestBase):
    def test_d12(self):
        for i in range (1,12):
            response = self.client.get(url_for('/d12'))
            self.assertIs(type(response.data.decode('utf-8')),int )
~                                                          
