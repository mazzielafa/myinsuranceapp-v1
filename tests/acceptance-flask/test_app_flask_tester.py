import json
import unittest
from project import app


class TestApp(unittest.TestCase):
    token=''
<<<<<<< HEAD

<<<<<<< HEAD
    def test_1_get_user_products(self):
        # return None
        tester = app.test_client(self)        
        print(f"token: {self.token}")
        headers = {"Authorization": f"Bearer {TestApp.token}"}        
        response = tester.get('/api/v1/users/1/products', content_type='application/json', headers=headers)       
        data=json.loads(response.text)        
        print(f"get_user_products: {data}")
        self.assertEqual(response.status_code, 200)       
        self.assertTrue(len(data)>0)
=======
=======
# In all methods we need to use the token
# GET METHOD 1 
>>>>>>> e701e902e5538b6c5bfe81da48836c176867bfc6
    def test_get_user_products(self):
        
        return None

<<<<<<< HEAD
>>>>>>> develop
    
=======

    #  Here we get the information of the client
    
# POST METHOD
    # Post a new user


>>>>>>> e701e902e5538b6c5bfe81da48836c176867bfc6
