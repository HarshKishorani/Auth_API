from flask_mongoengine import MongoEngine

#Creating a MongoEngine 
db = MongoEngine()

#Initializing a MongoDB for Application
def initialize_db(app):
    db.init_app(app)