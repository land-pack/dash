from flask import Flask
from flask import jsonify, make_response, request

from flask_cors import CORS

from data import lists as init_lists
from model import get_all_users, add_one


app = Flask(__name__)
CORS(app)


def to_render(x):
    r = make_response(jsonify(x))

    r.mimetype = 'application/json'
    r.headers['X-Total-Count'] = len(x)
    r.headers['Access-Control-Expose-Headers'] = "X-Total-Count"
    return r

@app.route("/users", methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"], defaults={'item': None})
@app.route("/users/<item>", methods=["OPTIONS", "GET", "POST", "PUT", "DELETE"])
def api_lists(item):
    #  X-Total-Count
    # return jsonify(lists)
    lists = init_lists
    print("Mehtod -->", request.method)
    if request.method == "GET":
        print("Get LIST")
        if item:
            return to_render(lists[int(item)])
        else:
            return to_render(get_all_users())

    elif request.method == "POST":
        print("POST New")
        # add_one()
        d = request.json
        print("post data --->", request.data)
        print("post data --->", request.json)

        print("before ..d----->", d)
        _id = add_one(d)
        print("d--sss-xxxx-->", d)
        d.update({"id": str(_id)})
        print("d---xxxx-->", d)
        return to_render(d)

    elif request.method == "PUT":
        if item:
            return to_render(lists[int(item)])
        else:
            return to_render(lists)
    elif request.method == "DELETE":
        lists = [
            x for x in lists if int(item) != x.get("id")
        ]
        return to_render(lists)
    else:
        return to_render(lists)

@app.route("/posts", methods=["OPTIONS", "GET", "POST"])
def api_posts():
    r = make_response(jsonify(lists))
    r.mimetype = 'application/json'
    r.headers['X-Total-Count'] = len(lists)
    r.headers['Access-Control-Expose-Headers'] = True
    return r
if __name__ == '__main__':
    app.run(debug=True, port=19001)