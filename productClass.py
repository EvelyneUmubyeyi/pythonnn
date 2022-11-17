from pathlib import Path


class Product:
    def __init__(self,name,ingredients,price,code,new=True):
        self.code = code
        self.name = name
        self.ingredients = ingredients
        self.price = price
        if new:
            file_name = Path('Menu_database.txt')
            file_name.touch(exist_ok=True)
            with open("Menu_database.txt") as file:
                lines = file.readlines()
            codes_list = []
            for line in lines:
                code, name, ingredients, price = line.split("@")
                codes_list.append(int(code))

            highest_code = 0
            for i in codes_list:
                if i > highest_code:
                    highest_code = i

            self.code = highest_code + 1
            lines.append(str(self.code)+"@"+self.name + "@" + self.ingredients + "@" + str(self.price) + "\n")

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
            code,name, ingredients, price = line.split("@")
            if code == self.code:
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

        lines.append(str(self.code)+"@"+self.name + "@" + self.ingredients + "@" + str(self.price) + "\n")
        with open("Menu_database.txt", "w") as file:
            for line in lines:
                file.write(line)

        print("Product updated successfully!")


# code = "004"
# name="Beef burger"
# ingredients = "Bread"
# price =9000
#
# prd = Product(code,name,ingredients,price)
# prd.update_menu_item()