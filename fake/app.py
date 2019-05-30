from flask import Flask
from flask import jsonify, make_response, request, redirect, url_for
from flask import abort

from flask_cors import CORS

from data import lists as init_lists
from model import get_all_users, add_one, find_one, remove_one, total_items


app = Flask(__name__)
CORS(app)


def to_render(data, total=None):
    # total = total if total else len(data)
    total = total_items()
    x = data or []
    if isinstance(x, list):

        [
            i.update({"id": str(i.get("_id")),
            "_id": str(i.get("_id"))
            })
            for i in x
        ]
    else:
        x = data or {}
        data.update({
            "_id": str(data.get("_id")),
            "id": str(data.get("_id"))
        })

    r = make_response(jsonify(x))

    r.mimetype = 'application/json'
    r.headers['X-Total-Count'] = total
    r.headers['Access-Control-Expose-Headers'] = "X-Total-Count"
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

    if request.method == "GET":
        print("Get LIST")
        if item is None:
            return to_render(get_all_users(_end=_end, _start=_start, _sort=_sort, _order=_order))
        elif len(item) > 5: # is MongoID 
            print("Get Item from[{}]".format(item))
            x = find_one(item)
            print("xxxxxxxxxxxx", x)
            return to_render(x) # if it's a instance , you can set total at init
        else:
            return to_render(get_all_users(_end=_end, _start=_start, _sort=_sort, _order=_order))

    elif request.method == "POST":
        print("POST New")
        # add_one()
        d = request.json
        _id = add_one(d)
        d.update({"id": str(_id)})
        data = {
            "data": d
        }
        return redirect("users/{}".format(_id))
        # return to_render(data)
        # return to_render(get_all_users(_end=_end, _start=_start, _sort=_sort, _order=_order))
        # return _id

    elif request.method == "PUT":
        x = find_one(item)
        return to_render(x)

        # if item:
        #     return to_render(lists[int(item)])
        # else:
        #     return to_render(lists)

    elif request.method == "DELETE":
        # lists = [
        #     x for x in lists if int(item) != x.get("id")
        # ]
        remove_one(item)
        return to_render(get_all_users())
    else:
        return to_render(lists)

@app.route("/posts", methods=["OPTIONS", "GET", "POST"])
def api_posts():
    r = make_response(jsonify(lists))
    r.mimetype = 'application/json'
    r.headers['X-Total-Count'] = len(lists)
    r.headers['Access-Control-Expose-Headers'] = True
    return r

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
    

if __name__ == '__main__':
    app.run(debug=True, port=19001)