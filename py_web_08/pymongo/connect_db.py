import configparser
from pymongo import MongoClient


config = configparser.ConfigParser()

config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')

connection_string = f"mongodb+srv://{mongo_user}:{mongodb_pass}@cluster.7tweqbb.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
