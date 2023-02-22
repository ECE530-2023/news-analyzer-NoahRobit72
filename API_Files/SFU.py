from flask import Flask
from flask_restful import Api, Resource

# API for Secure File Uploader Ingester
class SFU(Resource):
    def get(self):
        if(data.isempty()):
            return("ERROR: 400-level (Client error) client sent an invalid request")
        return {"data": "Secure file has been uploaded"}