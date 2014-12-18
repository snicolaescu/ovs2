from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_root():
    return "Hello, cyberworld!"


@app.route('/<name>', methods=['GET'])
def get_name(name):
    return "Hello, " + name + "!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)