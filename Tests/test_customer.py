import unittest
import sys
sys.path.append("../")
from models.Customer import Customer


class TestCustomerMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.Helena = Customer("Helena Nosrat", "500 Interstate Blvd", "Nashville", "TN", 37299, 6162124444,)


    def test_customer_is_instance(self):
        self.assertIsInstance(self.Helena, Customer)
