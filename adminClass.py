from userClass import *
from cafeteriaClass import Cafeteria

#menu = {"Beef burger": 3000, "Chips masala": 2500, "Chicken wings": 3000, "Chicken wrap": 3000, "Goat brochette": 1000, "Mango Fresh Juice": 1500, "Soda": 1000}

class Admin(User):
    passcode = "ABCDE"

    def __init__(self,name, email, password):
        super()._init_(name, email, password)
        self.role = "Admin"
        db = open("database.txt", "a")
        db.write(self.name + ", " + self.email + ", " + self.password + "\n")
        db.close()
        print("Account created successfully!")

    def addMenuItem(self):
        item = input("Enter item name: ")
        price = int(input("Enter item price: "))
        Cafeteria.menuItems[item] = price
        print("New menu: ")
        for item, price in Cafeteria.menuItems():
            print(item, ": ", price)

    def removeMenuItem(self):
        item = input("Enter item name: ")
        Cafeteria.menuItems.pop(item)
        print("New menu: ")
        for item, price in Cafeteria.menuItems():
            print(item, ": ", price)