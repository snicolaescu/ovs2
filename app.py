from flask import Flask

server = Flask(__name__)


@server.route('/', methods=['GET'])
def get_root():
    return "Hello, cyberworld!"


@server.route('/<name>', methods=['GET'])
def get_name(name):
    return "Hello, " + name + "!"


if __name__ == '__main__':
    server.run(host='127.0.0.1', port=80, debug=True)