from flask import Flask
from flask_restful import Api, Resource

class NLP(Resource):
    def get(self):
        if(data.isempty()):
            return("ERROR: 400-level (Client error) client sent an invalid request")
        return {"data": "Natural Language is processed!"}