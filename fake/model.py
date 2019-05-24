from db import db
# from pymongo.objectid import ObjectId
from bson.objectid import ObjectId

def get_all_users():
    lists = list(db.users.find({}))

    return lists

def add_one(x):
    user = db.users
    result = user.insert_one(x)
    _id = result.inserted_id
    print('One post: {0}'.format(_id))

    del x["_id"]
    return _id

def find_one(_id):
    user = db.users
    x = user.find_one({"_id": ObjectId(_id)})
    return x

if __name__ == '__main__':
    print(get_all_users())