from test import regex
from userClass import User
from orderClass import Order
from adminClass import Admin
from customerClass import Customer
from cafeteriaClass import Cafeteria
from productClass import Product
import bcrypt
import re
import sys
from pathlib import Path

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# login_user = ''


# Admin functionalities
def admin_actions(login_user):
    operation = int(input("Enter a number corresponding to an action you want to perform: \n"
                          "1.Add a menu item\n"
                          "2.Remove a menu item\n"
                          "3.Update a menu item\n"))
    if operation == 1:
        login_user.addMenuItem()
    elif operation == 2:
        login_user.removeMenuItem()
    elif operation == 3:
        login_user.update_menu_item()
    else:
        print("You entered an invalid choice!!")

# Customer functionalities
def takeOrder(item_code):
    file_name = Path('Menu_database.txt')
    file_name.touch(exist_ok=True)
    with open("Menu_database.txt") as file:
        lines = file.readlines()
    code_found = False
    for line in lines:
        code, name, ingredients, price = line.split("@")
        price = price.strip("\n")
        # print(code)
        if code == str(item_code):
            code_found = True
            order_item = Product(code,name,ingredients,price,False)
            quantity = int(input("How many would you like to order: "))
            # new_order.order_items.append([order_item,quantity])
            return [order_item,quantity]

    if code_found is False:
        print("You entered an invalid code!")

def print_menu(login_user):
    new_order = Order()
    while True:
        # print("Welcome, here is the Menu!")
        alu_cafe.printMenu()
        item_code = input("To make an order please enter a  code corresponding to your choice on the menu:")
        order = takeOrder(item_code)
        if order is not None:
            new_order.order_items.append(order)

        another_order = input("Enter Y if you would like to place another order or any other key if not: ")
        if another_order.upper() != "Y":
            break
    if len(new_order.order_items) != 0:
            new_order.checkout(login_user.email)
    else:
        choice = input("You can not proceed to check out without selecting a menu item Enter Y if you would like to"
                           " place an order or any other key to exit: ")
        if choice.upper() != "Y":
            sys.exit("Thank you!")
        else:
            print_menu(login_user)

def gainAccess():
    print("Welcome to Log in page!\n")
    login_email = input("Enter your email:")
    Password = input("Enter your Password:")
    data = ''
    if len(login_email) > 0 and len(Password) > 0:
        db = open("database.txt", "r")
        names = []
        emails = []
        passwords = []
        roles = []
        for i in db:
            name, email, password, title = i.split(",")
            names.append(name)
            email = email.strip()
            emails.append(email)
            password = password.strip()
            passwords.append(password)
            title = title.strip()
            roles.append(title)
        data = list(zip(names, emails, passwords, roles))
        result = ''
        email_exists = False
        for user in data:
            if user[1] == login_email:
                email_exists = True
                if user[3] == "admin":
                    login_user = Admin(user[0], user[1], user[2],False)
                    result = login_user.login(Password)
                elif user[3] == "customer":
                    login_user = Customer(user[0], user[1], user[2],False)
                    result = login_user.login(Password)

        if email_exists is False:
            print("Your email is not registered! Please sign up!")
            home()
        elif result == "success":
            print("Login successfull! Hi", login_user.name)
            if login_user.role == "customer":
                print_menu(login_user)
            elif login_user.role == "admin":
                admin_actions(login_user)
        elif result == "failed":
            print("Wrong password. Try again!")
            home()

def check_email(email):
    if (re.fullmatch(regex, email)):
        return "Valid Email"

    else:
        return "Invalid Email"


def register():
    print("Welcome to Sign up page!\n")
    while True:
        name = input("Enter your name:")
        email = input("Enter your email:")
        Password1 = input("Create password with at least 8 characters:")
        Password2 = input("Confirm Password:")
        user_role = ""
        role = int(input("Please choose a number corresponding to your role\n"
                         "1.Customer\n"
                         "2.Admin\n"))
        passcodeValid = True
        if role == 2:
            passcode = input("Please enter admin passcode: ")
            if passcode != Admin.passcode:
                passcodeValid = False
                # userRoleValid =False
            else:
                user_role = "Admin"
        elif role == 1:
            user_role = "Customer"

        else:
            userRoleValid = False

        email_valid = True
        if check_email(email) == "Invalid Email":
            email_valid = False

        file_name = Path('database.txt')
        file_name.touch(exist_ok=True)
        db = open("database.txt", "r")
        emails = []
        # Appending all emails in a list
        for i in db:
            registered_name, registered_email, password, registered_role = i.split(",")
            email = email.strip()
            emails.append(registered_email)
        db.close()
        email_exists = False
        for m in emails:
            if m == email:
                email_exists = True

        # Password in this case should be at least 8 characters
        if Password1 == Password2 and len(Password1) >= 8 and len(
                name) > 0 and email_valid and not email_exists and len(user_role) > 0:
            Password1 = Password1.encode('utf-8')
            Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())
            if user_role == "Customer":
                user = Customer(name, email, Password1)
            elif user_role == "Admin":
                user = Admin(name, email, Password1)
            break

        elif Password1 != Password2:
            print("Could not confirm password.")
        elif len(Password1) < 8:
            print("Password should be at least 8 characters.")
        elif len(name) == 0:
            print("Please provide your name!")
        elif not email_valid:
            print("Email format is wrong.")
        elif email_exists:
            print("Email is already registered. You can login!")
            # gainAccess()
            break
        elif not passcodeValid:
            print("You could not verify that you are an Admin. Please enter the passcode correctly or register as a"
                  "customer!")
        elif len(user_role) == 0:
            print("You did not choose a valid number corresponding to your role.")

        try_again = input("Enter Y if you would to try again or press any other key if you want to exit: ")
        if try_again.upper() != "Y":
            sys.exit("Thank you!")

    print("After registering, you should now log in to continue!")
    # gainAccess()

alu_cafe = Cafeteria()

def home():
    alu_cafe.cafe_details()
    option = int(input("1.Signup \n2.Login \nEnter your choice: "))
    if option == 1:
        register()
    elif option == 2:
        gainAccess()
    else:
        sys.exit("Invalid input! Try again you should enter 1 or 2.")



home()

