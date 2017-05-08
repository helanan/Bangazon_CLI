import unittest
from models.Customer import *

class TestCustomerMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
	       self.customer = {"name": "Jessica Jr", "address": "500 Interstate Blvd S", "phone_number": "615.555.1234"}

    def test_create_customer(self):

        create_customer(self.customer)
        # customer_id = get_customer_id(customer['name'], customer['address'], customer['phone'])
        customer_id = get_customer_id
        self.assertIsNotNone(customer_id)


    def test_activate_customer(self):

        create_customer(self.customer)
        customer_id = get_customer_id
        active_customer = activate_customer(customer_id)
        # active_customer = 1
        self.assertIsNotNone(active_customer)
