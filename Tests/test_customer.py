import unittest
from models.Customer import *
from models.payment_types import *

class TestCustomerMethods(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.customer = {"name": "Jessica Jr", "address": "500 Interstate Blvd S", "phone_number": "615.555.1234"}
		self.payment_type = {"account_name": "MasterCard", "account_number": "123456789098"}

	def test_create_customer(self):

		create_customer(self.customer["name"],self.customer["address"], self.customer["phone_number"])
		customer_id = get_customer_id(self.customer["name"],self.customer["address"], self.customer["phone_number"])
		self.assertIsNotNone(customer_id)


	def test_activate_customer(self):

		create_customer(self.customer["name"],self.customer["address"], self.customer["phone_number"])
		customer_id = get_customer_id(self.customer["name"],self.customer["address"], self.customer["phone_number"])
		active_customer = activate_customer(customer_id)
		# active_customer = 1
		self.assertIsNotNone(active_customer)

	def test_create_payment_type(self):
		create_customer(self.customer["name"],self.customer["address"], self.customer["phone_number"])
		customer_id = get_customer_id(self.customer["name"],self.customer["address"], self.customer["phone_number"])

		self.assertIsNotNone(customer_id)

		activate_customer(2)

		active_customer = activate_customer(self)

		self.assertIsNotNone(active_customer)

		create_payment_type(self.payment_type['account_name'], self.payment_type['account_number'], active_customer)

		payment_id = get_payment_type(self.payment_type['account_name'], self.payment_type['account_number'], active_customer)

		self.assertIsNotNone(payment_id)

	# def test_get_payment_types(self):
