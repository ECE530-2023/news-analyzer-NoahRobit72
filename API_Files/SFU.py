from flask import Flask
from flask_restful import Api, Resource

# API for Secure File Uploader Ingester
class SFU(Resource):
    def get(self):

        return {"data": "Secure file has been uploaded"}