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

class CustomerListApi(Resource):

    def get(self):
        model = Model('customers')
        d = to_json(model.get_all(), model.total_items())
        return d, 200, {"X-Total-Count": model.total_items(), "Access-Control-Expose-Headers":"X-Total-Count"}

    def post(self):
        model = Model('customers')
        d = request.json
        _id = model.add_one(d)
        d.update({"id": str(_id)})
        data = {
            "data": d
        }
        self.get()


class CustomersApi(Resource):

    def get(self, id):
        print("self._id", id)
        model = Model('customers')
        d = to_json(model.get_all(), model.total_items())
        return d[0], 200, {"X-Total-Count": model.total_items(), "Access-Control-Expose-Headers":"X-Total-Count"}

    def put(self, id):
        model = Model('customers')
        data = request.json
        x = model.update(id, data)
        return to_json(x)

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

    def put(self, id):
        model = Model('reviews')
        data = request.json
        x = model.update(id, data)
        return to_json(x)


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





class InvoicesApi(Resource):
    def get(self, id):
        model = Model('invoices')
        d = to_json(model.get_all(), model.total_items())
        return d[0], 200, {"X-Total-Count": model.total_items() , "Access-Control-Expose-Headers":"X-Total-Count"}

class InvoicesListApi(Resource):
    def get(self):
        model = Model('invoices')
        d = to_json(model.get_all(), model.total_items())
        return d, 200, {"X-Total-Count": model.total_items() , "Access-Control-Expose-Headers":"X-Total-Count"}

class CommandsApi(Resource):
    def get(self, id):
        model = Model('commands')
        # d = to_json(model.get_all(), model.total_items())
        d = to_json(model.find_one(id))

        return d, 200, {"X-Total-Count": model.total_items() , "Access-Control-Expose-Headers":"X-Total-Count", "Access-Control-Allow-Origin": "*"}

    def put(self, id):
        model = Model('commands')
        d = to_json(model.get_all(), model.total_items())
        return d[0]

class CommandsListApi(Resource):
    def get(self):
        model = Model('commands')
        d = to_json(model.get_all(), model.total_items())
        return d, 200, {"X-Total-Count": model.total_items() , "Access-Control-Expose-Headers":"X-Total-Count", "Access-Control-Allow-Origin": "*"}



api.add_resource(CustomerListApi, '/customers')
api.add_resource(CustomersApi, '/customers/<id>')
api.add_resource(ReviewsListApi, '/reviews')
api.add_resource(ReviewsApi, '/reviews/<id>')
api.add_resource(ProductsListApi, '/products')
api.add_resource(ProductsApi, '/products/<id>')
api.add_resource(CategoriesListApi, '/categories')
api.add_resource(CategoriesApi, '/categories/<id>')
api.add_resource(InvoicesListApi, '/invoices')
api.add_resource(InvoicesApi, '/invoices/<id>')
api.add_resource(CommandsListApi, '/commands')
api.add_resource(CommandsApi, '/commands/<id>')

if __name__ == '__main__':
    app.run(debug=True, port=19001)