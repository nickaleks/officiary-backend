from pymongo import MongoClient
import os

DB_PORT = 27017
DB_URL = os.environ.get('DB_URL')

client = MongoClient(host = DB_URL, port = DB_PORT)
db = client["database"]
declarations  = db["declarations"]
