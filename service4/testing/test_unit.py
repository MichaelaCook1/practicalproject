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

    def test_d20(self,mocked_randint):
        d20=self._make_one(sides=20)
        result = d20.roll()
        mocked_randint.assert_called_with(1,42)
        self.assertEqual



class Testd12(TestBase):
    def test_d12(self):
        12integers = [b"1",b"2",b"3",b"4",b"5",b"6",b"7",b"8",b"9",b"10",b"11",b"12"]
        response = self.client.get(url_for('d12'))
        self.assertIn(response.data, 12integers)

def even(self):
    response = self.client.post(
            url_for('total')
            data='32','30','28','26','24,'22,'20','18','16','14','12','10','8','6','4','2',
            follow_redirect=True
            )
    self.assertIn(b'You win a prize!',response.data)

def odd(self):
    response = self.client.post(
            url_for('total')
            data='31','29','27','25','23','21','19','17','15','13','11','9','7','5','3',
            follow_redirect=True
            )
    self.assertIn(b'You lose, try again!',response.data)
