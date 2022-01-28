from enum import unique
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

#Creating a User Model
class User(db.Document):
    email = db.EmailField(required = True)
    password = db.StringField(required = True)

    #Generating a hash/encrypted Password
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    #Checking the password for Login
    def check_password(self, password):
        return check_password_hash(self.password, password)