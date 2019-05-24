from pymongo import MongoClient
client = MongoClient()
from data import lists
db = client.pymongo_test


def add(x):
    user = db.users
    result = user.insert_one(x)
    print('One post: {0}'.format(result.inserted_id))
    printf("x is --->", x)

if __name__ == '__main__':
    # posts = db.posts
    # post_data = {
    #     'title': 'Python and MongoDB',
    #     'content': 'PyMongo is fun, you guys',
    #     'author': 'Scott'
    # }
    # result = posts.insert_one(post_data)
    # print('One post: {0}'.format(result.inserted_id))
    for x in lists:
        add(x)