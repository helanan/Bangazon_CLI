import sys
import sqlite3
from datetime import datetime
from time import time


# This method's purpose will not be needed once the CLI is working. The user will input the which customer they are selecting and it will be set to customer_id

def get_customer_id():
    return 1


def create_customer(name, address, city, c_state, zipcode, phone):
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

        c.execute("""INSERT INTO Customers values (?, ?, ?, ?, ?, ?, ?, ?)""", (None ,name, address, city, c_state, zipcode, phone))

        conn.commit()

def get_all_customers():

    ''' This method will retrieve all customers that are stored in the Customers table of bangazonData.db
    '''

    with sqlite3.connect('bangazonData.db') as conn:

        c = conn.cursor()

        c.execute("""SELECT * FROM Customers """)


        display_customers = c.fetchall()

        print(display_customers)

        try:
            return display_customers
        except:
            return None



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
