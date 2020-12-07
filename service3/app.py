from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

@app.route('/d12', methods=['GET'])
def d12():
    d12 = str(random.randint(1, 6))
    return Response(d12, mimetype="text/plain")

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)

