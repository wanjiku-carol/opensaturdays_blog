from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/payload', methods=['POST'])
def foo():
    data = json.loads(request.data)
    print("DATA RECEIVED:", data)
    return "OK"


if __name__ == '__main__':
    app.run(port=4567)
