from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'num_of_users': 0
})


class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, { "$set": {"num_of_users": new_num} } )
        return str("Hello user " + str(new_num))


def checkPostedData(postedData, functionName):
    if functionName == 'add' or functionName == 'subtract' or functionName == 'multiply':
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        else:
            return 200
    elif functionName == 'divide':
        if 'x' not in postedData or 'y' not in postedData:
            return 301
        elif postedData['y'] == 0:
            return 302
        else:
            return 200


class Add(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, 'add')

        if status_code != 200:
            res = {
                'message': 'An error occurred. Please check parameters again',
                'status code': status_code
            }
            return jsonify(res)

        x = int(postedData['x'])
        y = int(postedData['y'])
        res = {
            'sum': x + y,
            'status code': status_code
        }
        return jsonify(res)


class Subtract(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, 'subtract')

        if status_code != 200:
            res = {
                'message': 'An error occurred. Please check parameters again',
                'status code': status_code
            }
            return jsonify(res)

        x = int(postedData['x'])
        y = int(postedData['y'])
        res = {
            'sum': x - y,
            'status code': status_code
        }
        return jsonify(res)


class Multiply(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, 'multiply')

        if status_code != 200:
            res = {
                'message': 'An error occurred. Please check parameters again',
                'status code': status_code
            }
            return jsonify(res)

        x = int(postedData['x'])
        y = int(postedData['y'])
        res = {
            'sum': x * y,
            'status code': status_code
        }
        return jsonify(res)


class Divide(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedData(postedData, 'divide')

        if status_code != 200:
            res = {
                'message': 'An error occurred. Please check parameters again',
                'status code': status_code
            }
            return jsonify(res)

        x = float(postedData['x'])
        y = float(postedData['y'])
        res = {
            'sum': x / y,
            'status code': status_code
        }
        return jsonify(res)


@app.route('/')
def hello_world():
    return 'Hello World!'


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')
api.add_resource(Visit, '/hello')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
