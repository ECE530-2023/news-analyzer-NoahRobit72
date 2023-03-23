from flask import Flask
from flask_restful import Api, Resource
from SQL_Files.SQL_init import Init_Database

# Import the classes from the files
from API_Files.NLP import NLP
from API_Files.SFU import SFU
from API_Files.NFI import NFI

Init_Database()

app = Flask(__name__)
api = Api(app)
    
# Adding the paths and classes
api.add_resource(NLP, "/NLP")
api.add_resource(NFI, "/NFI")
api.add_resource(SFU, "/SFU")

# 

if __name__ == "__main__":
    app.run(debug=True)