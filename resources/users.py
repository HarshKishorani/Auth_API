from flask import Response
from database.models import User
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_restful import Resource

#Users Resource with GET method to return all the available Users with the bearer access token
class Users(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()# get id of user using bearer token 
        user= User.objects.get(id=user_id)# get Fetched by User
        users = User.objects().to_json()#get all the Users
        json_data = Response(users, mimetype="application/json").get_json()# Converting Response to JSON
        return {"Fetched By" : user.email,"data" : json_data}