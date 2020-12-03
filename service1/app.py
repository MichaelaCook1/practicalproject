#!/usr/bin/python3
from flask import Flask, render_template,request,url_for,redirect,Response
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import os



app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    #gets D20 result
    d20 = requests.get("http://service2:5001/d20")
    #gets D12 result
    d12 = requests.get("http://service3:5002/d12")
    #total
    value = int(d20.text)+ int(d12.text)
    result = requests.post("http://service4:5003/result", data=str(value))
    return render_template('index.html',d20=d20.text,d12=d12.text,value=value,result=result.text)


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')

