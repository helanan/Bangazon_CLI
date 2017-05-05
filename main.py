import os
import time


class BangazonUser():

  """ This class is the interface to the BangazonCLI
        Methods:
            main_menu
  """

  def __init__(self):
    self.account = None

  def build_menu(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*********************************************************")
    print("** Welcome to Bangazon! Command Line Ordering System :D **")
    print("*********************************************************")
    print("1. Create a customer account")
    print("2. Choose active customer")
    print("3. Create a payment option")
    print("4. Add product to shopping cart")
    print("5. Complete an order")
    print("6. Top 10 Products!")
    print("7. Exit Bangazon!, Come back soon!")


  def main_menu(self):
    """Show Bangazon! options
        Arguments: None
    """
    self.build_menu()
    choice = input(">> ")


    if choice == "1":

      first_name = input("Enter your first name")
      last_name = input("Enter youy last name")
      city = input("Enter your city")
      customer_state = input("Enter the state you live in")
      customer_zip_code = input("Enter your zip code")
      customer_phone_number = input("Enter your phone number")
      self.customer.create_user(first_name, last_name, city, customer_state, customer_zip_code, customer_phone_number, date_created)

    if choice == "2":
      customer_selection = input(self.customer.customer_list)

      self.customer.selected_customer(customer_selection)

    if choice == "3":
      print("1) Checking Account")
      print("2) Visa")
      print("3) MasterCard")
      print("4) American Express")
      print("5) Discovery")

      payment_type = input(">> ")
      card_information = input("Please enter your cards information")

      self.customer.add_payment_method(payment_type)


      payment_type = input("")

    if choice == "4":
        print(product_list)
      self.main_menu()


if __name__ == "__main__":
  Bangazon = BangazonUser()
  Bangazon.main_menu()
