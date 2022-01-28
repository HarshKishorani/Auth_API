from os import access
from flask import request
from database.models import User
from flask_restful import Resource, request
from flask_jwt_extended import create_access_token
import datetime


#Creating a Sign Up Resource with POST method request that returns the Id and email of the created User
class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id),'email' : body["email"]}, 200

#Log In Resource with POST method request that retuens a Log in token with 7 days expiry
class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))

        #If password is wrong
        if not authorized:
            return {"message": "Invalid username or password","status": 401}
    
        expires = datetime.timedelta(days=7)

        # create_access_token() function is used to actually generate the JWT token.
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token,'email' : body['email']}, 200


