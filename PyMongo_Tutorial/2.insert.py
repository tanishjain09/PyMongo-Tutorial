import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    db = client['tanish']
    collection = db['mySampleColletionForTanish']

    # insert one
    # dictonary = {'name' : 'tanish','marks':50}
    # collection.insert_one(dictonary)
    #
    # dictonary2  = {'name': 'tanish2', 'marks': 80}
    # collection.insert_one(dictonary2)

    #insert Many
    insertThese = [
        {'_id': 1, 'name': 'tanish', 'location': 'Baroda', 'marks': 59},
        {'_id': 2, 'name': 'akshat', 'location': 'Ghatol', 'marks': 60},
        {'_id': 3, 'name': 'vaibhai', 'location': 'Jaipur', 'marks': 58},
        {'_id': 4, 'name': 'nandini', 'location': 'Delhi', 'marks': 59}
    ]

    collection.insert_many(insertThese)