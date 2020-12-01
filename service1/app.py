from flask import Flask, render_template,request
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import os

app=Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

#defining database
class attempts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    result = db.Column(db.Boolean)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/roll', methods=['GET','POST'])
def index_roll():
    #persists results in database
    attempt=attempts.query.all()
    #gets D20 result
    d20 = requests.get("http://service2:5001/d20")
    #gets D12 result
    d12 = requests.get("http://service3:5002/d12")
    #total
    value = requests.post("http://service4:5003/value",data=value.text)
    resultcheck = requests.post("http://service4:5003/resultcheck", data=result.text)    
    if resultcheck == 'True':
        result = True
        attempt = attempts(
                value=value.text,
                result=result
        )
        db.session.add(attempt)
        db.session.commit()

    return render_template('index.html', d20=d20.text, d12=d12.text, total=total.text, attempts=attempt)

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')

