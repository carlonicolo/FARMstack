# import statements
from pymongo import MongoClient

# create DB connectio
#connection = MongoClient()
uri = "mongodb://karlitos:123@localhost/local?authSource=admin"
connection = MongoClient(uri)