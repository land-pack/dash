from db import db
# from pymongo.objectid import ObjectId
from bson.objectid import ObjectId
import pymongo

def total_items():
    user = db.users
    return user.count_documents({})

def get_all_users(_end=5, _order="DESC", _sort="id", _start=0):
    """
    _end=10&_order=DESC&_sort=id&_start=0
    """
    order_map = {
        "DESC": pymongo.DESCENDING,
        "ASC": pymongo.ASCENDING
    }

    limit = _end - _start
    result= db.users.find({}).skip(_start).sort([(_sort, order_map.get(_order))]).limit(limit)
    lists = list(result)

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

def remove_one(_id):
    user = db.users
    x = user.remove({"_id": ObjectId(_id)})
    return x

if __name__ == '__main__':
    print(get_all_users())