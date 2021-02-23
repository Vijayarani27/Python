from flask import Flask, jsonify, request
from flask_restful import Api,Resource, abort

app = Flask(__name__)
api = Api(app)

veggies = [
	{ 
	'Vegetable' :'carrot', 
	'Quantity':15
	},
{ 
	'Vegetable' : 'onion', 
	'Quantity': 17
	}
]

def abort_if_veg_doesnt_exist(name):
    count=0
    for veg in veggies:
        if name == veg['Vegetable']:
                count=1
    if count == 0:
          abort(404, message="Veg {} doesn't exist".format(name))


class Vegetable(Resource):
    def get(self):
        return jsonify(veggies)

    def post(self):
        dic = {}
        dic['Vegetable'] = request.json['Vegetable']
        dic['Quantity'] = request.json['Quantity']
        veggies.append(dic)
        return request.json


class Vegwitharg(Resource):
    def get(self,name):
        abort_if_veg_doesnt_exist(name)
        for veg in veggies:
            if name == veg['Vegetable']:
                return veg

    def delete(self,name):
        abort_if_veg_doesnt_exist(name)
        count=0
        for veg in veggies:
            if name == veg['Vegetable']:
                veggies.pop(count) 
                break
            count = count+1   
        return veg

    def put(self,name):
        abort_if_veg_doesnt_exist(name)
        for veg in veggies:
            if name == veg['Vegetable']:
                veg['Quantity'] = 22
                break  
        return veg

api.add_resource(Vegetable,'/vegetables')
api.add_resource(Vegwitharg,'/vegetables/<string:name>')
