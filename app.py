# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    result = a + b
    return jsonify(result=result)


@app.route('/subtract', methods=['GET'])
def subtract():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    result = a - b
    return jsonify(result=result)


@app.route('/multiply', methods=['GET'])
def multiply():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    result = a * b
    return jsonify(result=result)


@app.route('/divide', methods=['GET'])
def divide():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if b == 0:
        return jsonify(error="Cannot divide by zero"), 400
    result = a / b
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
