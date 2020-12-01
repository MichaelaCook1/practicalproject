from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase


from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestIndex(TestBase):
    def test_indexpage(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

class TestResponse(TestBase):
    def test_roll(self):
        with patch("requests.get") as g:
            g.return_value = "15"
            with patch("requests.get") as p:
                p.return_value = "4"
                with patch ("requests.post") as gp:
                    gp.return_value = "True"
                response = self.client.get(url_for("index_roll"))
                self.assertEqual(response.result, True)