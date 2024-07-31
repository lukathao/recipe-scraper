import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()
DBURL = os.getenv('MONGODB_URL')

def write_to_mongodb(items):
  print("writing to mongodb items: " + str(len(items)))
  # # Create a new client and connect to the server
  client = MongoClient(DBURL, server_api=ServerApi('1'))
  collections = client.get_database('food-recipes-db').get_collection('food-recipe-collections')

  try:
      collections.insert_many(items)
  except Exception as e:
      print('Error inserting item ')
      print(e)