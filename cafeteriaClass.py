class Cafeteria:
    """
    Initializing parent class
    """
    menuItems = {"Beef burger": 3000, "Chips masala": 2500, "Chicken wings": 3000, "Chicken wrap": 3000,
                      "Goat brochette": 1000,
                      "Mango fresh juice": 1500, "Soda": 1000}

    def printMenu(self):
        print(f"For today's menu, we have: \n")
        count = 1
        for item, price in self.menuItems.items():
            print(count, ". ", item, " = ", price, "RWF \n")
            count += 1


    def cafe_details(self):
        print("Welcome to ALU Cafeteria, a perfect place to promote healthy choices. your order will be available after thirty minutes")
        print("For new customers, please create a new account, and if you are an existing customer login to continue")
        print("1.Signup")
        print("2.Login")
        print("3.Exit")


#cafe = Cafeteria()
#cafe.printMenu()