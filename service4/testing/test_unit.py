from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestValue(TestBase):
    def test_value(self):
        with patch('requests.get') as g:
            g.return_value.text = "7"
            response = self.client.post(url_for('value'))
            self.assertIn(b'14',response.data)
    



