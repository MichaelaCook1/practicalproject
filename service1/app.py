from flask import Flask, render_template,request
import requests

app=Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    #gets D20 result
    d20 = request.get("http://service2:5001/d20")
    #gets D12 result
    d12 = request.get"http://service3:5002/d12")
    #total
    total = request.post("http://service4:5003/total",data=total.text)

    return render_template('index.html', d20=d20.text, d12=d12.text, total=total.text)

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')

