import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    db = client['tanish']
    collection = db['mySampleColletionForTanish']

    # one = collection.find_one({'name':'tanish'})
    # print(one)

    # allDocs = collection.find({'name':'tanish'},{'name':0,'_id':0}).limit(1)
    allDocs = collection.find({'name':'tanish','marks':{"$lte":80}},{'name':0,'_id':0})
    print(collection.count_documents({'name':'tanish'}))
    for item in allDocs:
        print(item)
