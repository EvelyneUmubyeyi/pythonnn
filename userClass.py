import bcrypt

user_records = []

class User:
    def _init_(self,name, email, password):
        self.name = name
        self.email = email
        self.password = str(password)
        self.role = ""
        # user_records.append(self)

    def login(self, password):
        hashed = self.password.strip('b')
        hashed = hashed.replace("'", "")
        hashed = hashed.encode('utf-8')
        if bcrypt.checkpw(password.encode(), hashed):
            return "success"
        else:
            return "failed"