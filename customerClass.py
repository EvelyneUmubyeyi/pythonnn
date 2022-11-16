from userClass import *

class Customer(User):
    def __init__(self, name, email, password):
        super()._init_(name, email, password)
        self.role = "Customer"

        db = open("database.txt", "a")
        db.write(self.name + ", " + self.email + ", "+ self.password + "\n")
        db.close()
        print("Account created successfully!")
        # print("Please refresh the page to login!")


