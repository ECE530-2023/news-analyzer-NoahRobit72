from flask import Flask
from flask_restful import Api, Resource

class NLP(Resource):
    def get(self):
        return {"data": "Natural Language is processed!"}