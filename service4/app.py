from flask import Flask, Response, request, jsonify
import requests
import random

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def result():
    value =int(request.data.decode('utf-8'))
    if (value % 2)==0:
        result = 'Win'
    else:
        result = "Lose"
    return Response(result, mimetype="text/plain")

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003) 
