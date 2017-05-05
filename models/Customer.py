import sys
import sqlite3
from datetime import datetime
from time import time

class Customer():

    def __init__(self, name, address, city, state, zipcode, phone):

        self.__name = name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zipcode
        self.__phone_number = phone
        self.__active = 0
        self.__id = None
