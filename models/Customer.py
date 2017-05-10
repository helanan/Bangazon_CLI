import sys
import sqlite3
from datetime import datetime
from time import time

def activate_customer():
    return 1

def get_customer_id():
    return 1


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

        c.execute("""INSERT INTO Customers values (?, ?, ?, ?, ?, ?, ?, ?)""", (None ,name, address, city, c_state, zipcode, phone, active))

        conn.commit()

def activate_customer(customer_id):

    ''' Allows the user select a customer from the active customer list and make set their status to 'active'

    Method Arguments:
        customer_id
    '''

    with sqlite3.connect('bangazonData.db') as conn:
        c = conn.cursor()


        c.execute("""SELECT c.Customer_id, c.name, c.address, c.city, c.c_state, c.zipcode, c.phone FROM Customers c WHERE c.Customer_id = ?""", [customer_id])


        active_customer = c.fetchone()

        try:
            return active_customer
        except:
            return None

# if __name__ == "__main__":
#     activate_customer(1)
