from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Pugs'


if __name__ == '__main__':
    app.run(host="localhost", port=9090, debug=True)
