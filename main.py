from userClass import *
from orderClass import *
from adminClass import *
from customerClass import *
# import bcrypt

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
    if order_item == 1:
        quantity = int(input("How many beef burgers do you want: "))
        item = ["Beef burger", menu["Beef burger"], quantity]
    elif order_item == 2:
        quantity = int(input("How many Chips masalas do you want: "))
        item = ["Chips masala", menu["Chips masala"], quantity]
    elif order_item == 3:
        quantity = int(input("How many Chicken wings do you want: "))
        item = ["Chicken wings", menu["Chicken wings"], quantity]
    elif order_item == 4:
        quantity = int(input("How many Chicken wraps do you want: "))
        item = ["Chicken wrap", menu["Chicken wrap"], quantity]
    elif order_item == 5:
        quantity = int(input("How many Goat brochettes do you want: "))
        item = ["Goat brochette", menu["Goat brochette"], quantity]
    elif order_item == 6:
        quantity = int(input("How many Mango Fresh Juices do you want: "))
        item = ["Mango Fresh Juice", menu["Mango Fresh Juice"], quantity]
    elif order_item == 7:
        quantity = int(input("How many sodas do you want: "))
        item = ["Soda", menu["Soda"], quantity]

    return item


# Start of the program
print("Welcome to ALU CAFETERIA")



def welcome():
    print("Welcome, here is the Menu!")


def gainAccess(name=None, Password=None):
    name = input("Enter your username:")
    Password = input("Enter your Password:")

    if not len(name or Password) < 1:
        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b # not used
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if name in data:
                    hashed = data[name].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')

                    try:
                        if bcrypt.checkpw(Password.encode(), hashed):

                            print("Login success!")
                            print("Hi", name)
                            welcome()
                        else:
                            print("Wrong password")

                    except:
                        print("Incorrect passwords or email")
                else:
                    print("This username  doesn't exist")
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

def register(name=None, email=None, Password1=None, Password2=None): # why parameters
    name = input("Enter your name:")
    email = input("Enter your email")
    Password1 = input("Create password:")
    Password2 = input("Confirm Password:")
    db = open("database.txt", "r")
    d = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        c = a, b   # Never used
        d.append(a)
    if not len(Password1) <= 8: # print to the user the length their password should be i.e more than 8 characters
        db = open("database.txt", "r")
        if not name == None:
            if len(name) < 1:
                print("Please provide your username")
                register()      # use a while loop instead that breaks when all conditions are met
            elif name in d:
                print("username exists")  # Check for email instead as it is more unique than names
                register()
            else:
                if Password1 == Password2:
                    Password1 = Password1.encode('utf-8')
                    Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())

                    db = open("database.txt", "a")
                    db.write(name + ", " + str(Password1) + "\n")  # include their email too
                    print("Account created successfully!")
                    print("Please refresh the page to login!")


                # print(texts)
                else:
                    print("The two Passwords do not match")
                    register()
    else:
        print("Your password is too short")


def home(option=None): # why parameter, why not use cafe_details, why not use a while loop until a valid input
    print("Welcome, please select an option")
    option = int(input("1.Signup \n2.Login \nEnter your choice: "))
    if option == 1:
        register()
    elif option == 2:
        gainAccess()
    else:
        print("Invalid input! enter the correct choice")


# register(Username, Password1, Password2)
# gainAccess(Username, Password1)
home()


user_role = []

# Creating users
if user_role == "Admin":
    new_user = Admin
elif user_role == "Customer":
    new_user = Customer
