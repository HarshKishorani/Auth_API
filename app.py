import imp
from flask import Flask, request, Response
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager

#Creating Flask Application
app = Flask(__name__)
#Creating API of the Application
api = Api(app)

#B-crypting the Application
bcrypt = Bcrypt(app)

# Setup the Flask-JWT-Extended extension 
app.config.from_pyfile('config.py')
jwt = JWTManager(app)

#Adding MongoDB Settings
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/auth'
}

#initialize_db function from db.py to 
initialize_db(app)
#Adding routes to the API
initialize_routes(api)

#Debug Mode
if __name__ == '__main__':
    app.run(debug = True)
