import unittest
import sys
sys.path.append('../models')
from Order import *
from Customer import *
from payment_types import *
# from models.Products import *

class TestOrderMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.order = {"customer_id" :3, "payment_id" :2, "active_status" :True, 'total': 1.00,'order_is_complete': 'Y', 'payment_type' :'Visa'}
        self.product = {"product_title" : "shoes", "product_price" :25, "product_description":"you can put this on your feet"}
        self.customer = {'customer_id' : 3}
        self.payment_type = {'payment_type' :'Visa','payment_id':1 }

    def test_product_is_added_to_shopping_cart(self):
        create_order(self.order)

        # this will add the order with it's stuff to the database
        order_id = get_order_id(self.order)
        product_id = get_product_id(self.product)
        # append product to order and add it to the database

        add_product_to_order(order_id, product_id)
        
        product_list = get_products_in_order(order_id)
        self.assertIn(product_id, product_list)
        # we need to assert our product is in the list

    
    def test_customer_order_total(self):
        create_customer(self.customer)
        customer_id = get_customer_id
        active_customer = activate_customer(customer_id)
        product_id = get_product_id(self.product)
        self.assertIsNotNone(product_id)
    
    def test_order_has_payment_type(self):
        create_customer(self.customer)
        customer_id = get_customer_id
        active_customer = activate_customer(customer_id)
        self.assertIsNotNone(active_customer)
        create_payment_type(self.payment_type)
        payment_type = get_payment_type(self.payment_type)
        self.assertIsNotNone(payment_type)


    def test_order_is_complete(self):
        create_customer(self.customer)
        customer_id = get_customer_id
        active_customer = activate_customer(customer_id)
        self.assertIsNotNone(active_customer)
        order_complete = get_payment_type(payment_id)
        payment_id = create_payment_type(self.payment_type)
        payment_type = get_payment_type(payment_id)
        self.assertIsNotNone(payment_id)
        create_order(self.order)
        order_complete = assertIsNotNone(customer_id, payment_id, product_id)
      
