from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

@app.route('/d12', methods=['GET'])
def d12():
    d12 = []
    d12 = random.randint(1, 12)
    d12.append(d12)
    return response(d12, mimetype="text/plain")

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)
