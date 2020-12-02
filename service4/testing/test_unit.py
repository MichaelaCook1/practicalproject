from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestValue(TestBase):
    def test_value(self)
    d20 = request.data.decode('utf-8')
    d12 = request.data.decode('utf-8')
    value =
