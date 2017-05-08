import unittest


class TestCustomerMethods(unittest.TestCase):

    def test_create_customer(self):

        customer = {
            'name': 'Gil',
            'address': '123 fleet st',
            'phone' : 8085851414
        }


        create_customer(customer)
        customer_id = get_customer_id(customer['name'], customer['address'], customer['phone'])
        self.assertIsNotNone(customer_id)


    def test_activate_customer(self):
        customer = {
            'name': 'Gil',
            'address': '123 fleet st',
            'phone' : 8085851414
        }
        create_customer(customer)
        customer_id = get_customer_id(customer['name'], customer['address'], customer['phone'])
        active_customer = activate_customer(customer_id)
        self.assertIsNotNone(active_customer)

        