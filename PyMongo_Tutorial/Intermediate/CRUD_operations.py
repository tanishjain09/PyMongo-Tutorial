from dotenv import load_dotenv,find_dotenv
import os 
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://intermediate:{password}@tutorial.sdiu8.mongodb.net/?retryWrites=true&w=majority&appName=tutorial"

client = MongoClient(connection_string)

dbs = client.list_database_names()

test_db = client.test
collections = test_db.list_collection_names()

print(collections)

def insert_test_doc():
    collections = test_db.test
    test_document = {
        "name":"Tanish",
        "type":"Test"
    }
    inserted_id = collections.insert_one(test_document).inserted_id
    print(inserted_id)

production = client.production
person_collection = production.person_collection

def create_document():
    first_name = ["Tanish","Akshat","Altaf","Kapil"]
    last_name = ["Sethiya","Lalawat","Mansuri","Patel"]
    ages = [19,20,20,21]
    docs= []
    
    for first_name,last_name,ages in zip(first_name,last_name,ages):
        doc = {"first_name":first_name,"last_name":last_name,"age":ages}
        docs.append(doc)
        # person_collection.insert_one(doc)
    person_collection.insert_many(docs)
    
printer = pprint.PrettyPrinter()

def find_all_people():
    people = person_collection.find()
    
    for person in people:
        printer.pprint(person)
        
# find_all_people()


def find_tanish():
    tanish = person_collection.find_one({"first_name":"Tanish"})
    printer.pprint(tanish)

# find_tanish()

def count_all_person():
    count = person_collection.count_documents(filter={})
    print("Number of people",count)

# count_all_person()

def get_person_by_id(person_id):
    from bson.objectid import ObjectId
    
    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id":_id})
    printer.pprint(person)

# get_person_by_id("67d2cc61b92e65dbee333475")
