from dotenv import load_dotenv,find_dotenv
import os
import pprint
from pymongo import MongoClient
from datetime import datetime as dt
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://intermediate:{password}@tutorial.sdiu8.mongodb.net/?retryWrites=true&w=majority&appName=tutorial&authSource=admin"
client = MongoClient(connection_string)

dbs = client.list_database_names()
production = client.production

# schema validation

def create_book_colection():
  book_validator = {
    "$jsonSchema": {
      "bsonType": "object",
      "required": ["title", "authors", "publish_date", "type", "copies"],
      "properties": {
        "title": {
          "bsonType": "string",
          "description": "must be a string and is required"
        },
        "authors": {
          "bsonType": "array",
          "items": {
            "bsonType": "objectId",
            "description": "must be an objectid and is required"
          }
        },
        "publish_date": {
          "bsonType": "date",
          "description": "must be a date and is required"
        },
        "type": {
          "enum": ["Fiction", "Non-Fiction"],
          "description": "can only be one of the enum values and is required"
        },
        "copies": {
          "bsonType": "int",
          "minimum": 0,
          "description": "must be an integer greater than 0 and is required"
        },
      }
    }
  }

  try:
      production.create_collection("book")
  except Exception as e:
      print(e)

  production.command("collMod","book",validator=book_validator)


def create_author_collection():
  author_validator = {
    "$jsonSchema": {
      "bsonType": "object",
      "required": ["first_name", "last_name", "date_of_birth"],
      "properties": {
        "first_name": {
          "bsonType": "string",
          "description": "must be a string and is required"
        },
        "last_name": {
          "bsonType": "string",
          "description": "must be a string and is required"
        },
        "date_of_birth": {
          "bsonType": "date",
          "description": "must be a date and is required"
        }
      }
    }
  }
  try:
    production.create_collection("author")
  except Exception as e:
    print(e)

  production.command("collMod","author",validator=author_validator)

# create_author_collection()

def create_data():
  authors = [
    {
      "first_name":"Tanish",
      "last_name":"Sethiya",
      "date_of_birth":dt(2005,9,9)
    },
    {
      "first_name":"Altaf",
      "last_name":"Mansuri",
      "date_of_birth":dt(2004,8,31)

    },
    {
      "first_name":"Akshat",
      "last_name":"Lalawat",
      "date_of_birth":dt(2004,12,26)
    },
    {
      "first_name":"Kapil",
      "last_name":"Patel",
      "date_of_birth":dt(2003,10,16)
    }
  ]
  author_collection = production.author
  authors = author_collection.insert_many(authors).inserted_ids

