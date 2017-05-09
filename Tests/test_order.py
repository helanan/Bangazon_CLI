import unittest
from models.Order import *

class TestOrderMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
    	self.order = {"customer_id" : 3, "payment_id" : 2, "active_status" : True}
    	self.product = {"product_title" : "shoes", "product_price" : 25, "product_description" : "you can put this on your feet"}

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


        