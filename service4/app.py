from flask import Flask, Response, request, jsonify
import random

app = Flask(__name__)

@app.route('/total', methods=['POST'])
def total():
    d20 = request.data.decode('utf-8')
    d12 = request.data.decode('utf-8')
    value = d12+d20
    if value%2==0:
        total = "You win a prize!"
    else:
        total = "You lose, try again!"

    return response(total, mimetype="text/plain")

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
~                                                 
