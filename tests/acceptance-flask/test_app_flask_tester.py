import json
import unittest
from project import app



class TestApp(unittest.TestCase):
    token=''

    def test_get_user_products(self):
        # tester = app.test_client(self)
        # user_data = {"fullname", "email", "birthdate", "country", "city", "address", "password" }
        
        # How I would write this out in postman
        # response = tester.get("/api/v1/users/product", content_type='application/json', headers=headers)
        # data=json.loads(response.data)
        # self.assertEqual(response.status_code,200)

        return None
        # ['fullname']
        # email = request.form['email']
        # birthdate = request.form['birthdate']
        # country = request.form['country']
        # city = request.form['city']
        # address = request.form['address']
        # password = request.form['password']