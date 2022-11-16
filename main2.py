from test import regex
from userClass import *
from orderClass import *
from adminClass import *
from customerClass import *
import bcrypt
import re
import sys

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Admin functionalities
def changeMenu():
    operation = int(input("Enter a number corresponding to an action you want to perform: \n"
                          "1.Add a menu item\n"
                          "2.Remove a menu item\n"))
    if operation == 1:
        new_user.addMenuItem()
    elif operation == 2:
        new_user.removeMenuItem()
    else:
        print("You entered an invalid choice!!")

# Customer functionalities
def placeAnOrder():
    item = ""
    order_item = int(
        input("To make an order please choose from the list and enter a number corresponding to your choice: \n"
              "1. Beef burger = 3000rwf\n"
              "2. Chips masala = 2500rwf\n"
              "3. Chicken wings = 3000rwf\n"
              "4. Chicken wrap = 3000rwf\n"
              "5. Goat brochette = 1000rwf\n"
              "6. Mango fresh Juice = 1500rwf\n"
              "7. Soda = 1000rwf\n"))
    # if order_item == 1:
    #     quantity = int(input("How many beef burgers do you want: "))
    #     item = ["Beef burger", menu["Beef burger"], quantity]
    # elif order_item == 2:
    #     quantity = int(input("How many Chips masalas do you want: "))
    #     item = ["Chips masala", menu["Chips masala"], quantity]
    # elif order_item == 3:
    #     quantity = int(input("How many Chicken wings do you want: "))
    #     item = ["Chicken wings", menu["Chicken wings"], quantity]
    # elif order_item == 4:
    #     quantity = int(input("How many Chicken wraps do you want: "))
    #     item = ["Chicken wrap", menu["Chicken wrap"], quantity]
    # elif order_item == 5:
    #     quantity = int(input("How many Goat brochettes do you want: "))
    #     item = ["Goat brochette", menu["Goat brochette"], quantity]
    # elif order_item == 6:
    #     quantity = int(input("How many Mango Fresh Juices do you want: "))
    #     item = ["Mango Fresh Juice", menu["Mango Fresh Juice"], quantity]
    # elif order_item == 7:
    #     quantity = int(input("How many sodas do you want: "))
    #     item = ["Soda", menu["Soda"], quantity]
    #
    # return item


# Start of the program
print("Welcome to ALU CAFETERIA")



def welcome():
    print("Welcome, here is the Menu!")


def gainAccess(name=None, Password=None):
    print("Welcome to Log in page!\n")
    while True:
        email = input("Enter your email:")
        Password = input("Enter your Password:")
        data=''
        if len(name) > 0 and len(Password) > 0:
            db = open("database.txt", "r")
            names = []
            emails = []
            passwords = []
            for i in db:
                name, email, password = i.split(",")
                email = email.strip()
                emails.append(email)
                password = password.strip()
                passwords.append(password)
                data = list(zip(name,email,password))
                print(data)
            try:
                if email in emails:

                    hashed = data[email].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')

                    try:
                        if bcrypt.checkpw(Password.encode(), hashed):
                            print("Login success!")
                            print("Hi", name)
                            welcome()
                        else:
                            print("Wrong password. Try again!")

                    except:
                        print("Incorrect passwords or email")
                else:
                    print("Email not registered. Please register")
                    registered = False
            except:
                print("Password or username doesn't exist")
        else:
            print("Error logging into the system")

        else:
            print("Please attempt login again")
            gainAccess()
        loginStatus = ""
        for user in user_records:
            if user.name == name:
                loginStatus = user.login(password)
                break
        if loginStatus == "success" and user_role == "Customer":
            new_order = Order()
            item = placeAnOrder()
            new_order.order_items.append(item)

            while True:
                repeat = input(
                    "Enter 1 if you want to place another order or any other key if you have no further orders: ")
                if repeat != "1":
                    break
                item = placeAnOrder()
                new_order.order_items.append(item)
                new_order.checkout()
        # # b = b.strip()


# accessDb()

def check_email(email):
    if (re.fullmatch(regex, email)):
        return "Valid Email"

    else:
        return "Invalid Email"


def register():
    print("Welcome to Sign up page!\n")
    while True:
        name = input("Enter your name:")
        email = input("Enter your email")
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

        db = open("database.txt", "r")
        d = []
        # Appending all emails in a list
        for i in db:
            a, b, c = i.split(",")
            b = b.strip()
            d.append(b)
        db.close()
        email_exists = False
        for m in d:
            if m == email:
                email_exists = True


        # Password in this case should be at least 8 characters
        if Password1 == Password2 and len(Password1) >= 8 and len(name)>0 and email_valid and not email_exists and len(user_role)>0:
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
        elif len(name)>0:
            print("Please provide your name!")
        elif not email_valid:
            print("Email format is wrong.")
        elif email_exists:
            print("Email is already registered. You can login!")
            gainAccess()
            break
        elif not passcodeValid:
            print("You could not verify that you are an Admin. Please enter the passcode correctly or register as a"
                  "customer!")
        elif len(user_role) == 0:
            print("You did not choose a valid number corresponding to your role.")

        try_again = input("Enter Y if you would to try again or press any other key if you want to exit: ")
        if try_again.upper() != "Y":
            sys.exit()

    print("After registering, you should now log in to continue!")
    gainAccess()


def home(option=None):
    print("Welcome, please select an option")
    option = int(input("1.Signup \n2.Login \nEnter your choice: "))
    if option == 1:
        register()
    elif option == 2:
        gainAccess()
    else:
        sys.exit("Invalid input! Try again you should enter 1 or 2.")


# register(Username, Password1, Password2)
# gainAccess(Username, Password1)
home()


user_role = []

# Creating users
if user_role == "Admin":
    new_user = Admin
elif user_role == "Customer":
    new_user = Customer
