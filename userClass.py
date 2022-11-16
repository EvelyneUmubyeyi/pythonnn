user_records = []

class User:
    def _init_(self,name, email, password):
        self.name = name
        self.email = email
        self.password = str(password)
        self.role = ""
        user_records.append(self)

    def login(self, password):
        if self.password == password:
            return "success"
        else:
            return "failed"