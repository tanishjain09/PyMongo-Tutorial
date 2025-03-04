import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    db = client['tanish']
    collection = db['mySampleColletionForTanish']
    prev = {'name':'vaibhai'}
    nextt = {"$set":{'location':'ajmer'}}
    collection.update_one(prev,nextt)
    #update_many -> update all name


