import unittest
import sys
sys.path.append('../models')
from models.Order import *
from models.Customer import *
from models.payment_types import *

class TestOrderMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.order = {
        'order_id': 1,
        "customer_id":3,
        'payment_id':2,
        'active_status':True,
        'total': 1.00,
        'payment_type' :'Visa'}

        self.product = {
        "product_title":"shoes",
        "product_price" :25,
        "product_description":"you can put this on your feet"}

        self.customer = {
        'customer_id' : 3}

        self.payment_type = {
        'account_number':'1234567890',
        'account_name': 'Amex',
        'payment_id':1 }

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

        customer_id = get_customer_id()
        active_customer = activate_customer(customer_id)
        product_id = get_product_id(self.product)
        self.assertIsNotNone(product_id)
    
    def test_order_has_payment_type(self):

        customer_id = get_customer_id()
        active_customer = activate_customer(customer_id)
        self.assertIsNotNone(active_customer)
        active_customer = get_customer_payment_type(customer_id)
        self.assertIsNotNone(customer_id)


    def test_order_is_complete(self):
 
        customer_id = get_customer_id()
        active_customer = activate_customer(customer_id)
        self.assertIsNotNone(active_customer)
        # create an order- adds it to our database
        create_order(self.order)
        # adds payment type to our database
        account_number = get_customer_payment_type(customer_id)
        # retrieves our orderid from order we made
        order_id = get_order_id(self.order)
        payment_id = get_payment_type_id(self.payment_type)
        # attach a payment type to order
        add_payment_to_order(payment_id, order_id)
        # adds payment to or order using the order id
        complete_order_payment_type = get_payment_type_from_order(order_id)
       # assert the payment type is there
        self.assertIsNotNone(complete_order_payment_type)

