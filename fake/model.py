from db import db
# from pymongo.objectid import ObjectId
from bson.objectid import ObjectId
import pymongo

class Model(object):
    def __init__(self, col_name="users"):
        self.col = db[col_name]

    def total_items(self):
        return self.col.count_documents({})

    def get_all(self, _end=5, _order="DESC", _sort="id", _start=0):
        """
        _end=10&_order=DESC&_sort=id&_start=0
        """
      
        order_map = {
            "DESC": pymongo.DESCENDING,
            "ASC": pymongo.ASCENDING
        }

        limit = _end - _start

        result= self.col.find({}).skip(_start).sort([(_sort, order_map.get(_order))]).limit(limit)
        lists = list(result)

        return lists

    def add_one(self, x):
        result = self.col.insert_one(x)
        _id = result.inserted_id
        print('One post: {0}'.format(_id))

        del x["_id"]
        return _id

    def find_one(self, _id):
        x = self.col.find_one({"_id": ObjectId(_id)})
        return x

    def update(self, _id, data):
        if "_id" in data:
            del data['_id']
        self.col.update({'_id': ObjectId(_id)}, {"$set": data}, upsert = True)
        x = self.col.find_one({"_id": ObjectId(_id)})
        return x

    def remove_one(self, _id):
        x = self.col.remove({"_id": ObjectId(_id)})
        return x


if __name__ == '__main__':
    print(get_all_users())