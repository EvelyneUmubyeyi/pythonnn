from pathlib import Path


class Product:
    def __init__(self,name,ingredients,price):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        file_name = Path('Menu_database.txt')
        file_name.touch(exist_ok=True)
        with open("Menu_database.txt") as file:
            lines = file.readlines()

        lines.append(self.name + "@" + self.ingredients + "@" + str(self.price) + "\n")

        with open("Menu_database.txt", "w") as file:
            for line in lines:
                file.write(line)

        print("Product created successfully!")

    def update_menu_item(self):
        file_name = Path('Menu_database.txt')
        file_name.touch(exist_ok=True)
        with open("Menu_database.txt") as file:
            lines = file.readlines()

        for line in lines:
            name, ingredients, price = line.split("@")
            if name == self.name:
                lines.remove(line)

        change_name = input("Do you want to change product name? Enter Y if yes or any other key if no: ")
        if change_name.upper() == "Y":
            new_name = input("Enter new name: ")
            self.name = new_name
        change_ingredients = input("Do you want to change product ingredients? Enter Y if yes or any other key if no: ")
        if change_ingredients.upper() == "Y":
            new_ingredients = input("Enter new ingredients: ")
            self.ingredients = new_ingredients
        change_price = input("Do you want to change product price? Enter Y if yes or any other key if no: ")
        if change_price.upper() == "Y":
            new_price = input("Enter new price: ")
            self.price = new_price

        lines.append(self.name + "@" + self.ingredients + "@" + str(self.price) + "\n")
        with open("Menu_database.txt", "w") as file:
            for line in lines:
                file.write(line)

        print("Product updated successfully!")

# prd = Product("burger","Chicken,Onions",2500)
# prd.update_menu_item()