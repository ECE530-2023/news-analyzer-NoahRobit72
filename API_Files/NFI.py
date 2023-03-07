from flask import Flask
from flask_restful import Api, Resource

class NFI(Resource):
    def get(self):
        return {"data": "News feed has been injested"}
    