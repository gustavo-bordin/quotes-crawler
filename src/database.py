from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


class Database:
    def __init__(self):
        self.connection = self.connect()
        self.database = self.connection.quotes
        self.collection = self.database.quotes

    def connect(self):
        try:
            return MongoClient('mongodb://{}:{}@{}:{}'.format(
                DB_USER, DB_PASS, DB_HOST, DB_PORT
            ))
        except errors.ConnectionFailure:
            print('Server not available: {}'.format(errors.ConnectionFailure))

    def insert(self, quotes):
        self.collection.insert_many(quotes)
