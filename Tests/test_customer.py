import unittest
from models.Customer import *
from models.Bangazon_Operator import *

class TestCustomerMethods(unittest.TestCase):



    def test_create_customer(self):
        customer = create_customer("Jessica Jr", "500 Interstate Blvd S", "Nashville", "TN", "37209", "6155551234")
        # customer_id = get_customer_id(customer['name'], customer['address'], customer['phone'])
        customer_id = get_customer_id
        self.assertIsNotNone(customer_id)


    def test_activate_customer(self):

        customer_id = get_customer_id
        active_customer = activate_customer(customer_id)
        # active_customer = 1
        self.assertIsNotNone(active_customer)
