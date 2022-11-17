from userClass import User
from cafeteriaClass import Cafeteria
from productClass import Product
from pathlib import Path


#menu = {"Beef burger": 3000, "Chips masala": 2500, "Chicken wings": 3000, "Chicken wrap": 3000, "Goat brochette": 1000, "Mango Fresh Juice": 1500, "Soda": 1000}

class Admin(User):
    passcode = "ABCDE"

    def __init__(self,name, email, password):
        super()._init_(name, email, password)
        self.role = "Admin"
        file_name = Path('database.txt')
        file_name.touch(exist_ok=True)
        with open("database.txt") as file:
            lines = file.readlines()

        lines.append(self.name + ", " + self.email + ", " + self.password + ", admin\n")

        with open("database.txt", "w") as file:
            for line in lines:
                file.write(line)

        print("Admin created successfully!")

    def addMenuItem(self):
        item = input("Enter item name: ")
        ingredients = input("Enter item ingredients: ")
        price = int(input("Enter item price: "))
        new_product = Product(item,ingredients,price)

    def removeMenuItem(self):
        item = input("Enter item name: ")
        file_name = Path('Menu_database.txt')
        file_name.touch(exist_ok=True)
        with open("Menu_database.txt") as file:
            lines = file.readlines()

        for line in lines:
            name, ingredients, price = line.split("@")
            if name == item:
                lines.remove(line)

        with open("Menu_database.txt", "w") as file:
            for line in lines:
                file.write(line)

# adm = Admin("Adu","adu@gmail.com","b'$2b$12$NMn5KjSnvTyu1GhihZszP.6hs5kP5Viyj9ruGZjZ.Tz9KkQVUJfuK'")
# adm.removeMenuItem()
