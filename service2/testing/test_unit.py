from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class Testd20(TestBase):
    def test_d20(self):
        for i in range (1,20):
            self.assertIs(self.number,int)
        response = self.client.get(url_for('d20'))
        self.assertIn(response.data, 20integers)
