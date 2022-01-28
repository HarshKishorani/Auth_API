from .auth import SignupApi,LoginApi
from .users import Users

#Adding Resources and Routes from classes extending Resource 
def initialize_routes(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi,'/api/auth/login')
    api.add_resource(Users,'/api/all-users')
