import unittest
from models.Order import *
from models.Customer import *
from models.Payment import *
from models.Products import *

class TestOrderMethods(unittest.TestCase):
    ''' Test for if an order has a 'total(price)',
    test if and order has a payment type, and test if an order is complete.

    created: 2017
    author: Miriam Rozenbaum 
    '''
    @classmethod
    def setUpClass(self):
        self.order = {'total': 1.00,'customer_order_complete': 'Y'}
        self.customer = {'Customer_id': 1}
        self.payment = {'payment_type': 'Visa','payment_id': 1}
        self.product = {'product_price': 20.00,'product_id': 1}

    
    def test_customer_order_total(self):
        create_customer(self.customer)
        customer_id = get_customer_id
        active_customer = activate_customer(customer_id)
        product_id = get_product_id(product_id)
        self.assertIsNotNone(product_id)
    
    def test_order_has_payment_type(self):
        create_customer(self.customer)
        customer_id = get_customer_id
        active_customer = active_customer(customer_id)
        self.assertIsNotNone(active_customer)
        create_payment(self.payment)
        payment_type = get_payment_type(payment_id)
        self.assertIsNotNone(payment_id)


    def test_order_is_complete(self):
        create_customer(self.customer)
        customer_id = get_customer_id
        active_customer = active_customer(customer_id)
        self.assertIsNotNone(active_customer)
        create_payment(self.payment)
        payment_type = get_payment_type(payment_id)
        self.assertIsNotNone(payment_id)
        order_complete = assertIsNotNone(customer_id, payment_id, product_id)
      