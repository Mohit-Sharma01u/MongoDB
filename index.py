import pymongo
# x = mongodb://localhost:27017/

if __name__ == "__main__" :
    print("Welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

db = client['Mohit']
coll = db['mySampleCollectionForMohit']

data = {'name' : 'mohit', 'marks' : 45}
coll.insert_one(data)

# data1 = {'name' : 'king', 'marks' : 99}

# coll.insert_one(data1)

v1 = coll.find({},{"_id" : 0})

for i in v1 :
    print(i)
