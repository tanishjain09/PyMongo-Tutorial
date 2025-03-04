import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client['tanish']
    collection = db['mySampleColletionForTanish']

    #delete one
    # rec = {'name':'vaibhavi','adress':'ajmer'}
    # collection.delete_one(rec)

    #delete many
    rec = {'name':'tanish','marks':50}
    delete = collection.delete_many(rec)
    print(delete.deleted_count)

