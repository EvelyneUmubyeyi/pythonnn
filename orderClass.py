class Order:
    def _init_(self):
        self.order_items = []
        self.total_price = 0

    def checkout(self):
        for item in self.order_items:
            self.total_price += item[1]*item[2]

        self.printOrder()
        print("The total price is: ", self.total_price, " Rwf")
        confirm = int(input("to confirm your order enter 1: \n"))
        if confirm == 1:
            print("\n your order has been confirmed!")
            print("Please come after 30minutes to collect your order. "
                  "You can pay using our momo code *182*8*1*9845#, Thank you!!")
        else:
            print("Your order has been removed from the cart!, refresh to make a new order!")

    def printOrder(self):
        print("You ordered: \n")
        for item in self.order_items:
            print(item[2], " ", item[0], ": ", item[1]*item[2], " Rwf")