#!/usr/bin/python3
from flask import Flask, render_template,request,url_for,redirect
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import os

app=Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.246.12.217/attempts'
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#defining database
class attempts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    result = db.Column(db.Boolean)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index_roll', methods=['GET','POST'])
def index_roll():
    #persists results in database
    attempt=attempts.query.all()
    #gets D20 result
    d20 = requests.get("http://service2:5001/d20")
    #gets D12 result
    d12 = requests.get("http://service3:5002/d12")
    #total
    value = requests.get("http://service4:5003/value")
    resultcheck = requests.post("http://service4:5003/resultcheck")    
    if resultcheck == 'True':
        result = True
        attempt = attempts(
                value=value.text,
                result=result
        )
        db.session.add(attempt)
        db.session.commit()

    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')

