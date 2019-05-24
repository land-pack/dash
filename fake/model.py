from db import db


def get_all_users():
    return list(db.users.find({}, {'_id': False}))

def add_one(x):
    user = db.users
    result = user.insert_one(x)
    _id = result.inserted_id
    print('One post: {0}'.format(_id))

    del x["_id"]
    return _id


if __name__ == '__main__':
    print(get_all_users())