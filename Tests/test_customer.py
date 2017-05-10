import unittest
from models.Customer import *
from models.payment_types import *

class TestCustomerMethods(unittest.TestCase):


    def test_create_customer(self):
        customer = create_customer("Jessica Jr", "500 Interstate Blvd S", "Nashville", "TN", "37209", "6155551234")
        # customer_id = get_customer_id(customer['name'], customer['address'], customer['phone'])
        customer_id = get_customer_id()
        self.assertIsNotNone(customer_id)


    def test_activate_customer(self):

        customer_id = get_customer_id()
        active_customer = activate_customer(customer_id)
        # active_customer = 1
        self.assertIsNotNone(active_customer)

class TestPaymentMethods(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.customer = {"name": "Jessica Jr", "address": "500 Interstate Blvd S", "city": "Nashville", "c_state": "TN", "zipcode": "37209", "phone": "615.555.1234"}
		self.payment_type = {"account_name": "MasterCard", "account_number": "123456789098"}

	def test_create_payment_type(self):

		customer_id = get_customer_id()
		self.assertIsNotNone(customer_id)

		active_customer = activate_customer(customer_id)
		self.assertIsNotNone(active_customer)

		create_payment_type(self.payment_type['account_name'], self.payment_type['account_number'], active_customer)
		payment_id = get_payment_type(self.payment_type['account_name'], self.payment_type['account_number'])
		self.assertIsNotNone(payment_id)

	def test_get_all_payment_types_for_customer(self):
		customer_id = get_customer_id()

		create_payment_type(self.payment_type['account_name'], self.payment_type['account_number'], customer_id)
		all_customer_payment_types = get_customer_payment_type(customer_id)
		self.assertTrue(len(all_customer_payment_types) > 0)



	def test_select_payment_type(self):
		customer_id = get_customer_id()
		self.assertIsNotNone(customer_id)

		active_customer = activate_customer(customer_id)
		self.assertIsNotNone(active_customer)

		create_payment_type(self.payment_type['account_name'], self.payment_type['account_number'], active_customer)
		payment_id = get_customer_payment_type(customer_id)
		self.assertIsNotNone(payment_id)

		customer_payment_types = get_customer_payment_type(active_customer)
		self.assertIsNotNone(customer_payment_types)

		selected_payment_type = set_payment_type(payment_id)
