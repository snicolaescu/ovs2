from flask import Flask, jsonify, request, abort

server = Flask(__name__)


@server.route('/', methods=['GET'])
def get_root():
    return "Hello, cyberworld!"


@server.route('/<name>', methods=['GET'])
def get_name(name):
    return "Hello, " + name + "!"


@server.route('/ovs/orders', methods=['POST'])
def validate_order():
    print "HEY: " + str(request.json)
    if (request.json['address'] == ""):
        return jsonify({'error': 'address field is empty'}), 400
    if (request.json['name'] == ""):
        return jsonify({'error': 'name field is empty'}), 400
    if (request.json['productType'] == ""):
        return jsonify({'error': 'orderType field is empty'}), 400
    
    
    return str(request.json)
    



if __name__ == '__main__':
    server.run(host='127.0.0.1', port=80, debug=True)