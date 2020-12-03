from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class Testvalue(TestBase):
    def test_value(self):
        response = self.client.get('/value')
        value=response.data.decode('utf-8').isnumeric() and int(response.data.decode('utf-8'))>=2 and int(response.data.decode('utf-8'))<=32
        self.assertFalse(value)


