from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase


from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_d20_on_page(self):
        with patch("requests.get") as g:
            with patch("requsts.post") as p:
                g.return_value.text = "20"
                p.return_value.text = "20"


                response = self.client.get(url_for("index"))
                self.assertIn(b'20 20',response.data)
