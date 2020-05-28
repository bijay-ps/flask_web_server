from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if functionName == 'add':
        if 'x' not in postedData or 'y' not in postedData:
            return 301
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
    pass


class Multiply(Resource):
    pass


class Divide(Resource):
    pass


@app.route('/')
def hello_world():
    return 'Hello World!'


api.add_resource(Add, '/add')

if __name__ == '__main__':
    app.run()
