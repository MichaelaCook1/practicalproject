from flask import Flask, Response, request, jsonify
import requests
import random

app = Flask(__name__)

@app.route('/value', methods=['POST'])
def value():
    d20 = request.data.decode('utf-8')
    d12 = request.data.decode('utf-8')
    value = d12+d20
    return response(value,mimetype='text/plain')

@app.route('/resultcheck', methods=['POST']
        def resultcheck():
        value =int(request.data.decode('utf-8'))
        result = 'False'
            if (value % 2)==0:
                result = 'False'
            else:
                result = "True"
            return response(result, mimetype="text/plain")

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
~                                                 
