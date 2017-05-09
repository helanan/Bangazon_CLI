import sys
import sqlite3
from datetime import datetime
from time import time

def create_customer(name, address, city, c_state, zipcode, phone, active=False):
    ''' Allows the user to add a customer to the database

        Method Arguments:
            name,
            address,
            city,
            c_state,
            zipcode,
            phone

    '''

    with sqlite3.connect('bangazonData.db') as conn:
        c = conn.cursor()


        name = name
        address = address
        city = city
        c_state = c_state
        zipcode = zipcode
        phone = phone
        active = "false"

        c.execute("""INSERT INTO Customers values (?, ?, ?, ?, ?, ?, ?, ?)""", (None ,name, address, city, c_state, zipcode, phone, active))

        conn.commit()

def test_active_customer(Customer_id):

    ''' Allows the user select a customer from the active customer list and make set their status to 'active'

        Method Arguments:
            Customer_id
        '''
