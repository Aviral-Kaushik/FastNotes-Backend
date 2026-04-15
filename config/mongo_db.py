from pymongo import MongoClient

MONGO_URI: str = "mongodb://localhost:27017/fastNotes" 

conn = MongoClient(MONGO_URI)