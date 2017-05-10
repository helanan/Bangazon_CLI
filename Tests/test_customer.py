import unittest
from models.Customer import *
from models.Bangazon_Operator import *
from models.payment_types import *

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

class TestPaymentMethods(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.customer = {"name": "Jessica Jr", "address": "500 Interstate Blvd S", "city": "Nashville", "c_state": "TN", "zipcode": "37209", "phone": "615.555.1234"}
		self.payment_type = {"account_name": "MasterCard", "account_number": "123456789098"}

	def test_create_payment_type(self):

		self.payment_type = {"account_name": "MasterCard", "account_number": "123456789098"}
		create_customer(self.customer["name"], self.customer['address'], self.customer["city"], self.customer["c_state"], self.customer["zipcode"], self.customer["phone"])
		customer_id = get_customer_id

		self.assertIsNotNone(customer_id)

		activate_customer(2)

		active_customer = activate_customer(self)

		self.assertIsNotNone(active_customer)

		create_payment_type(self.payment_type['account_name'], self.payment_type['account_number'], active_customer)

		payment_id = get_payment_type(self.payment_type['account_name'], self.payment_type['account_number'], active_customer)

		self.assertIsNotNone(payment_id)
