from flask import Flask
from flask_restful import Api, Resource

class NLP(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        
        # adding name and ID to NLP analysis 
        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('name', required=True)
        
        return {"data": "Natural Language is processed!"}