import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()
DBURL = os.getenv('MONGODB_URL')

def write_to_mongodb(item):
  print(item)
  print("writing to mongodb")
  print(DBURL)

  # # Create a new client and connect to the server
  client = MongoClient(DBURL, server_api=ServerApi('1'))
  collections = client.get_database('food-recipes-db').get_collection('food-recipe-collections')

  try:
      collections.insert_one(item)
  except Exception as e:
      print('Error inserting item ' + item)
      print(e)