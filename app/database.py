from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("DATABASE_URL")

client = MongoClient(MONGODB_URL)
db = client.get_default_database()
print(db)

def get_database():
    return db