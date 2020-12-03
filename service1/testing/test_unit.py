from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app
from application import db
from application.models import attempts

class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"
        app.config['SECRET_KEY']='TEST_SECRET_KEY'
        app.config['DEBUG']=True
        return app
    
    def setUp(self):
        db.create_all()
        id1 = attempts(id='1')
        value1 = attempts(value='12')
        result1 = attempts(value= 'Win')
        db.session.add(id1)
        db.session.add(value1)
        db.session.add(result1)
        db.session.commit()
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestIndex(TestBase):
    def test_indexpage(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)


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
            


