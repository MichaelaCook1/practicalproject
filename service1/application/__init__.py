from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@34.89.21.101/attempts'
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


from application import routes
