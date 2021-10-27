from flask import Flask
import pymongo


app = Flask(__name__)
app.config["SECRET_KEY"] = "9053ec8968f39c8c633ed333064468cad835e301"
app.config["MONGO_URI"] = "mongodb+srv://Search-DB:shu12wedfcV@cluster0.igzqx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongo_client = pymongo.MongoClient(app)
db = mongo_client.db

from application import routes
