from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

@app.route('/d20', methods=['GET'])
def d20():
    d20 = str(random.randint(1, 6))
    return Response(d20, mimetype="text/plain")

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

