from flask import Blueprint
from flask_restful import Api, Resource


class Hello(Resource):
    def get(self):
        return {"message": "Hello World!"}


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Hello, '/')
