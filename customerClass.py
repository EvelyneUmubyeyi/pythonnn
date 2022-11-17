from userClass import *
from pathlib import Path


class Customer(User):
    def __init__(self, name, email, password, new=True):
        super()._init_(name, email, password)
        self.role = "customer"
        if new:
            file_name = Path('database.txt')
            file_name.touch(exist_ok=True)
            with open("database.txt") as file:
                lines = file.readlines()

            lines.append(self.name + ", " + self.email + ", " + self.password + ", customer\n")

            with open("database.txt", "w") as file:
                for line in lines:
                    file.write(line)

            print("Customer created successfully!")


# cus = Customer("Adeline","adeline@gmail.com","b'$2b$12$NMn5KjSnvTyu1GhihZszP.6hs5kP5Viyj9ruGZjZ.Tz9KkQVUJfuK'")
