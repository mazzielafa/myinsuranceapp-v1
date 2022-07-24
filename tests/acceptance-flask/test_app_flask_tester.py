import json
import unittest
from project import app


class TestApp(unittest.TestCase):
    token=''

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
    