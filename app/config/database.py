from pymongo import MongoClient


client = MongoClient("mongodb+srv://admin:dz2szn2mTOG7WR5K@cluster0.xbcyuq8.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]