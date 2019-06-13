from flask import Flask
from flask import jsonify, make_response, request, redirect, url_for
from flask import abort

from flask_cors import CORS
from flask_restful  import Resource, Api, reqparse, abort

from data import lists as init_lists
from model import Model


app = Flask(__name__)
CORS(app)

api = Api(app)

def to_json(data, total=None):
    total = total if total else len(data)
    # total = total_items()
    x = data or []
    if isinstance(x, dict):
        x = data or {}
        data.update({
            "_id": str(data.get("_id")),
            "id": str(data.get("_id"))
        })
    else:
        [
            i.update({"id": str(i.get("_id")),
            "_id": str(i.get("_id"))
            })
            for i in x
        ]
    return x

def to_render(data, total=None):
    x = to_json(data, total)
    r = make_response(jsonify(x))

    r.mimetype = 'application/json'
    r.headers['X-Total-Count'] = total
    r.headers['Content-Rang'] = "items 0-24/900"
    r.headers['Access-Control-Expose-Headers'] = "Content-Rang"
    return r

@app.route("/users", methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"], defaults={'item': None})
@app.route("/users/<item>", methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"])
def api_lists(item):
    #  X-Total-Count
    # return jsonify(lists)
    lists = init_lists
    print("Mehtod -->", request.method, request.args.get("_end"))
    _end = int(request.args.get("_end", 10))
    _start = int(request.args.get("_start", 0))
    _sort = request.args.get("_sort")
    _order = request.args.get("_order")
    model = Model('users')
    if request.method == "GET":
        print("Get LIST")
        if item is None:
            return to_render(model.get_all(_end=_end, _start=_start, _sort=_sort, _order=_order), model.total_items())
        elif len(item) > 5: # is MongoID 
            print("Get Item from[{}]".format(item))
            x = model.find_one(item)
            print("xxxxxxxxxxxx", x)
            return to_render(x) # if it's a instance , you can set total at init
        else:
            return to_render(model.get_all(_end=_end, _start=_start, _sort=_sort, _order=_order), model.total_items())

    elif request.method == "POST":
        print("POST New")
        # add_one()
        d = request.json
        _id = model.add_one(d)
        d.update({"id": str(_id)})
        data = {
            "data": d
        }
        return redirect("users/{}".format(_id))
        # return to_render(data)
        # return to_render(get_all_users(_end=_end, _start=_start, _sort=_sort, _order=_order))
        # return _id

    elif request.method == "PUT":
        x = model.find_one(item)
        return to_render(x, model.total_items())

        # if item:
        #     return to_render(lists[int(item)])
        # else:
        #     return to_render(lists)

    elif request.method == "DELETE":
        # lists = [
        #     x for x in lists if int(item) != x.get("id")
        # ]
        model.remove_one(item)
        return to_render(model.get_all(), model.total_items())
    else:
        return to_render(lists)

@app.route("/posts", methods=["OPTIONS", "GET", "POST"])
def api_posts():
    # r = make_response(jsonify(init_lists))
    # r.mimetype = 'application/json'
    # r.headers['X-Total-Count'] = len(init_lists)
    # r.headers['Content-Range'] = len(init_lists)
    # # r.headers['Access-Control-Expose-Headers'] = True
    # r.headers['Access-Control-Expose-Headers'] = "X-Total-Count"
    model = Model('course')
    return to_render(model.get_all(), model.total_items())

@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    # r = make_response(jsonify(lists))
    # r.mimetype = 'application/json'
    # r.headers['X-Total-Count'] = len(lists)
    # r.headers['Access-Control-Expose-Headers'] = True
    print(request.json)
    # return jsonify({"token":"xxxx"})
    data = request.json or {}

    username = data.get("username")
    print(username)
    if username == 'username':
        return jsonify({"token":"xxxx"})
    else:
        abort(403)

@app.route("/course", methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"], defaults={'item': None})
@app.route("/course/<item>", methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"])
def courses(item):
    #  X-Total-Count
    # return jsonify(lists)
    # lists = init_lists
    print("Mehtod -->", request.method, request.args.get("_end"))
    _end = int(request.args.get("_end", 10))
    _start = int(request.args.get("_start", 0))
    _sort = request.args.get("_sort")
    _order = request.args.get("_order")

    # if request.method == "GET":
    #     print("Get LIST")
    #     if item is None:
    #         return to_render(get_all_users(_end=_end, _start=_start, _sort=_sort, _order=_order))
    #     elif len(item) > 5: # is MongoID 
    #         print("Get Item from[{}]".format(item))
    #         x = find_one(item)
    #         print("xxxxxxxxxxxx", x)
    #         return to_render(x) # if it's a instance , you can set total at init
    #     else:
    model = Model('course')

    if request.method == "POST":
        d = request.json
        _id = model.add_one(d)
        d.update({"id": str(_id)})
        data = {
            "data": d
        }
        return redirect("course/{}".format(_id))
    elif request.method == "GET":
        print("Get LIST")
        if item is None:
            return to_render(model.get_all(_end=_end, _start=_start, _sort=_sort, _order=_order), model.total_items())
        elif len(item) > 5: # is MongoID 
            print("Get Item from[{}]".format(item))
            x = model.find_one(item)
            print("xxxxxxxxxxxx", x)
            return to_render(x) # if it's a instance , you can set total at init
        else:
            return to_render(model.get_all(_end=_end, _start=_start, _sort=_sort, _order=_order), model.total_items())

    return to_render(model.get_all(), model.total_items())


@app.route("/blogHome", methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"], defaults={'item': None})
@app.route("/blogHome/<item>", methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"])
def blog_home(item):
    #  X-Total-Count
    # return jsonify(lists)
    # lists = init_lists
    print("Mehtod -->", request.method, request.args.get("_end"))
    _end = int(request.args.get("_end", 10))
    _start = int(request.args.get("_start", 0))
    _sort = request.args.get("_sort")
    _order = request.args.get("_order")

    # if request.method == "GET":
    #     print("Get LIST")
    #     if item is None:
    #         return to_render(get_all_users(_end=_end, _start=_start, _sort=_sort, _order=_order))
    #     elif len(item) > 5: # is MongoID 
    #         print("Get Item from[{}]".format(item))
    #         x = find_one(item)
    #         print("xxxxxxxxxxxx", x)
    #         return to_render(x) # if it's a instance , you can set total at init
    #     else:
    model = Model('course')

    if request.method == "POST":
        d = request.json
        _id = model.add_one(d)
        d.update({"id": str(_id)})
        data = {
            "data": d
        }
        return redirect("course/{}".format(_id))
    elif request.method == "GET":
        print("Get LIST")
        if item is None:
            return to_render(model.get_all(_end=_end, _start=_start, _sort=_sort, _order=_order), model.total_items())
        elif len(item) > 5: # is MongoID 
            print("Get Item from[{}]".format(item))
            x = model.find_one(item)
            print("xxxxxxxxxxxx", x)
            return to_render(x) # if it's a instance , you can set total at init
        else:
            return to_render(model.get_all(_end=_end, _start=_start, _sort=_sort, _order=_order), model.total_items())

    return to_render(model.get_all(), model.total_items())


@app.route("/customersx", methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"], defaults={'item': None})
@app.route("/customersx/<item>", methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"])
def customers(item):
    #  X-Total-Count
    # return jsonify(lists)
    # lists = init_lists
    print("Mehtod -->", request.method, request.args.get("_end"))
    _end = int(request.args.get("_end", 10))
    _start = int(request.args.get("_start", 0))
    _sort = request.args.get("_sort")
    _order = request.args.get("_order")

    # if request.method == "GET":
    #     print("Get LIST")
    #     if item is None:
    #         return to_render(get_all_users(_end=_end, _start=_start, _sort=_sort, _order=_order))
    #     elif len(item) > 5: # is MongoID 
    #         print("Get Item from[{}]".format(item))
    #         x = find_one(item)
    #         print("xxxxxxxxxxxx", x)
    #         return to_render(x) # if it's a instance , you can set total at init
    #     else:
    model = Model('customers')

    if request.method == "POST":
        d = request.json
        _id = model.add_one(d)
        d.update({"id": str(_id)})
        data = {
            "data": d
        }
        return redirect("course/{}".format(_id))
    elif request.method == "GET":
        print("Get LIST")
        return to_render(model.get_all(), model.total_items())
        # if item is None:
        #     return to_render(model.get_all(_end=_end, _start=_start, _sort=_sort, _order=_order), model.total_items())
        # elif len(item) > 5: # is MongoID 
        #     print("Get Item from[{}]".format(item))
        #     x = model.find_one(item)
        #     print("xxxxxxxxxxxx", x)
        #     return to_render(x) # if it's a instance , you can set total at init
        # else:
        #     return to_render(model.get_all(_end=_end, _start=_start, _sort=_sort, _order=_order), model.total_items())

    return to_render(model.get_all(), model.total_items())

class HelloWorld(Resource):
    def get(self):
        d = model.get_all(), model.total_items()
        return {"hello": "world"}


parser = reqparse.RequestParser()
parser.add_argument('task')


class CustomerListApi(Resource):

    def get(self):
        model = Model('customers')
        d = to_json(model.get_all(), model.total_items())
        return d, 200, {"X-Total-Count": model.total_items(), "Access-Control-Expose-Headers":"X-Total-Count"}


class CustomersApi(Resource):

    def get(self, id):

        print("self._id", id)
        model = Model('customers')
        d = to_json(model.get_all(), model.total_items())
        return d[0], 200, {"X-Total-Count": model.total_items(), "Access-Control-Expose-Headers":"X-Total-Count"}

    def put(self):
        model = Model('customers')
        d = to_json(model.get_all(), model.total_items())
        return d[0]

class ReviewsListApi(Resource):
    def get(self):
        model = Model('reviews')
        d = to_json(model.get_all(), model.total_items())
        return d, 200, {"X-Total-Count": model.total_items() , "Access-Control-Expose-Headers":"X-Total-Count"}

class ReviewsApi(Resource):
    def get(self, id):
        model = Model('reviews')
        d = to_json(model.get_all(), model.total_items())
        return d[0], 200, {"X-Total-Count": model.total_items() , "Access-Control-Expose-Headers":"X-Total-Count"}


class ProductsListApi(Resource):
    def get(self):
        model = Model('products')
        d = to_json(model.get_all(), model.total_items())
        return d, 200, {"X-Total-Count": model.total_items() , "Access-Control-Expose-Headers":"X-Total-Count"}

class CategoriesApi(Resource):
    def get(self, id):
        model = Model('categories')
        d = to_json(model.get_all(), model.total_items())
        return d[0], 200, {"X-Total-Count": model.total_items() , "Access-Control-Expose-Headers":"X-Total-Count"}

class CategoriesListApi(Resource):
    def get(self):
        model = Model('categories')
        d = to_json(model.get_all(), model.total_items())
        return d, 200, {"X-Total-Count": model.total_items() , "Access-Control-Expose-Headers":"X-Total-Count"}

class ProductsApi(Resource):
    def get(self, id):
        model = Model('products')
        d = to_json(model.get_all(), model.total_items())
        return d[0], 200, {"X-Total-Count": model.total_items() , "Access-Control-Expose-Headers":"X-Total-Count"}



class CommandsApi(Resource):
    def get(self):
        return [], 200, {"X-Total-Count": 0, "Access-Control-Expose-Headers":"X-Total-Count"}


api.add_resource(HelloWorld, '/hello')
api.add_resource(CustomerListApi, '/customers')
api.add_resource(CustomersApi, '/customers/<id>')
api.add_resource(CommandsApi, '/commands')
api.add_resource(ReviewsListApi, '/reviews')
api.add_resource(ReviewsApi, '/reviews/<id>')
api.add_resource(ProductsListApi, '/products')
api.add_resource(ProductsApi, '/products/<id>')
api.add_resource(CategoriesListApi, '/categories')
api.add_resource(CategoriesApi, '/categories/<id>')

if __name__ == '__main__':
    app.run(debug=True, port=19001)