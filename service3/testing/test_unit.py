from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class Testd12(TestBase):
    def test_d12(self):
        12integers = [b"1",b"2",b"3",b"4",b"5",b"6",b"7",b"8",b"9",b"10",b"11",b"12"]
        response = self.client.get(url_for('d12'))
        self.assertIn(response.data, 12integers)
~                                                          
