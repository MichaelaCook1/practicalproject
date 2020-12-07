from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app
from application import db
from application.models import __init__
from application.models import attempts


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_rollwin(self):
        with patch("requests.get") as g:
            g.return_value = "7"
            with patch ("requests.post") as p:
                p.return_value.text = "Win"

        
    def test_rollwin(self):
        with patch("requests.get") as g:
            g.return_value = "8"
            with patch ("requests.post") as p:
                p.return_value.text = "Lose"
            


