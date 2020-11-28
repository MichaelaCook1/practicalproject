from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class Testd20(TestBase):
    def test_d20(self):
        20integers = [b"1",b"2",b"3",b"4",b"5",b"6",b"7",b"8",b"9",b"10",b"11",b"12",b"13",b"14",b"15",b"16",b"17",b"18",b"19",b"20"]
        response = self.client.get(url_for('d20'))
        self.assertIn(response.data, 20integers)
