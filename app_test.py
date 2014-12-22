import unittest
from app import server

class OVSTest(unittest.TestCase):
    
    def setUp(self):
        self.applications = server.test_client()
    
    
    def test_root(self):
        name = 'manuel'
        result = self.applications.get('/' + name)
        assert "Hello, " + name + "!" == result.data
        
    def test_order_validation(self):
        order = {
                 'name': 'manuel',
                 'address': 'one vz way',
                 'productType': 'Hey'
                 }
        result = self.applications.post('/ovs/orders', content_type='application/json', data=order)
        print result.status
        assert "200" in result.status
        
        order = {
                 'name': '',
                 'address': 'one vz way',
                 'productType': 'Hey'
                 }
        result = self.applications.post('/ovs/orders', data=order)
        assert 400 == result.code and {'error': 'name is empty'} == result.data
        
        order = {
                 'name': 'manuel',
                 'address': '',
                 'productType': 'Hey'
                 }
        result = self.applications.post('/ovs/orders', data=order)
        assert 400 == result.code and {'error': 'address is empty'} == result.data
        
        order = {
                 'name': 'manuel',
                 'address': 'One VZ Way',
                 'productType': ''
                 }
        result = self.applications.post('/ovs/orders', data=order)
        assert 400 == result.code and {'error': 'productType is empty'} == result.data
        
        

if __name__ == '__main__':
    unittest.main()