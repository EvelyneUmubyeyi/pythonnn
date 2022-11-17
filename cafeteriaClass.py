from pathlib import Path


class Cafeteria:

    # menuItems = {"Beef burger": 3000, "Chips masala": 2500, "Chicken wings": 3000, "Chicken wrap": 3000,
    #                   "Goat brochette": 1000,
    #                   "Mango fresh juice": 1500, "Soda": 1000}

    # menuItems = []

    def printMenu(self):
        print(f"For today's menu, we have: \n")
        file_name = Path('Menu_database.txt')
        file_name.touch(exist_ok=True)
        with open("Menu_database.txt") as file:
            lines = file.readlines()

        # count = 1
        for line in lines:
            name, ingredients, price = line.split("@")
            price = price.strip("\n")
            print("Name: ", name)
            print("Ingredients: ", ingredients)
            print(f"Price: {price} RWF")
            print("-------------------------------------------------")


    def cafe_details(self):
        print("Welcome to ALU Cafeteria, a perfect place to promote healthy choices. your order will be available after thirty minutes")
        print("For new customers, please create a new account, and if you are an existing customer login to continue")


# cafe = Cafeteria()
# cafe.printMenu()