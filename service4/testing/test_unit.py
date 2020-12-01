from flask import url_for
from flask_testing import TestCase
from mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app
class Testd20(TestBase):
    def gen_d20(self, *args, **kw):
        from app import d20
        return d20(*args, **kw)

    def TestApi(TestBase):
        def test_checkresult(self):
            response = self.client.post('/checkresult', data='13')
            self.assertIN(b'True', response.data)
