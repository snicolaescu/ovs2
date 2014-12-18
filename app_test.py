import unittest
from app import server

class OVSTest(unittest.TestCase):
    
    def setUp(self):
        self.applications = server.test_client()
    
    
    def test_root(self):
        name = 'manuel'
        result = self.applications.get('/' + name)
        assert "Hello, " + name + "!" == result.data
        

if __name__ == '__main__':
    unittest.main()