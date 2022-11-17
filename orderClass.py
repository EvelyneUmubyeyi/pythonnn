from pathlib import Path
from productClass import *


class Order:
    order_items = []
    total_price = 0

    # def _init_(self):

    def checkout(self,email):
        file_name = Path('Orders_database.txt')
        file_name.touch(exist_ok=True)
        with open("Orders_database.txt") as file:
            lines = file.readlines()

        order_string = email+"#"
        for item in self.order_items:
            order_string += item[0].name+"`"+str(item[1])+"^"
            self.total_price += int(item[0].price)*item[1]

        order_string = order_string[:-1]
        order_string += "%" + str(self.total_price)+"\n"
        lines.append(order_string)

        self.printOrder()
        print("The total price is: ", self.total_price, " Rwf")
        confirm = int(input("to confirm your order enter 1: \n"))
        if confirm == 1:
            with open("Orders_database.txt", "w") as file:
                for line in lines:
                    file.write(line)
            print("\n your order has been confirmed!")
            print("Please come after 30minutes to collect your order. "
                  "You can pay using our momo code *182*8*1*9845#, Thank you!!")
        else:
            print("Your order has been removed from the cart!, refresh to make a new order!")

    def printOrder(self):
        print("You ordered: \n")
        for item in self.order_items:
            print(item[1], " ", item[0].name, ": ", int(item[0].price)*item[1], " Rwf")

# prd = Product("burger","Chicken,Onions",2500)
# prd_two = Product("nuggets","Chicken,Onions",2500)
# order_one = Order()
# order_one.order_items.append([prd,2])
# order_one.order_items.append([prd_two,3])
# order_one.checkout("eve@gmail.com")

