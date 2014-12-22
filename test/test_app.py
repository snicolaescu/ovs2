import unittest
import json
from app import server
from flask import jsonify

class OVSTest(unittest.TestCase):
    
    def setUp(self):
        self.applications = server.test_client()


    def test_root(self):
        result = self.applications.get('/')
        assert 'OK' == result.data
        
    def test_valid_orders(self):
        # Testing productType: SONET
        order = '{"name": "John Smith", "address": "One Verizon Way, Basking Ridge, NJ, 07920", "productType": "SONET"}'
        result = self.applications.post('/ovs/orders', content_type='application/json', data=order)
        json_result = json.loads(result.data)
        assert 200 == result.status_code

        # Testing productType: FiOS
        order = '{"name": "John Smith", "address": "One Verizon Way, Basking Ridge, NJ, 07920", "productType": "FiOS"}'
        result = self.applications.post('/ovs/orders', content_type='application/json', data=order)
        json_result = json.loads(result.data)
        # Check Results
        assert 200 == result.status_code

    def test_invalid_orders(self):
        # Testing empty order
        order = '{}'
        result = self.applications.post('/ovs/orders', content_type='application/json', data=order)
        json_result = json.loads(result.data)
        # Check Results
        assert 400 == result.status_code
        assert 'error' in json_result
        assert 'order is empty' == json_result['error']

    def test_order_creation(self):
        # Create order
        order = '{"name": "John Smith", "address": "One Verizon Way, Basking Ridge, NJ, 07920", "productType": "FiOS"}'
        result_post = self.applications.post('/ovs/orders', content_type='application/json', data=order)
        json_result_post = json.loads(result_post.data)
        # Check Results from POST
        assert 200 == result_post.status_code
        # Get the order again via GET
        result_get = self.applications.get('/ovs/orders/' + json_result_post['id'])
        json_result_get = json.loads(result_get.data)
        # Check Results from GET
        assert 200 == result_get.status_code
        assert json_result_post == json_result_get['order']



    def test_invalid_orders(self):
        # Testing empty order
        order = '{}'
        result = self.applications.post('/ovs/orders', content_type='application/json', data=order)
        json_result = json.loads(result.data)
        assert 400 == result.status_code and 'error' in json_result and 'order is empty' == json_result['error']

if __name__ == '__main__':
    unittest.main()