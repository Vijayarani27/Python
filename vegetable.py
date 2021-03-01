from flask import Flask, request,abort,make_response,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api,Resource
from marshmallow import fields
from marshmallow.validate import Range, Length
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
import jwt
import datetime
from functools import wraps
import os

app=Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'PUBLICINSECURESECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Vegetable.sqlite3'
api=Api(app)


db =SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     public_id = db.Column(db.Integer)
     name = db.Column(db.String(50))
     password = db.Column(db.String(50))
     admin = db.Column(db.Boolean)

class vegetable(db.Model):
    vegname=db.Column(db.String(80), primary_key=True)
    qty=db.Column(db.Integer)

    def __repr__(self):
        return '<vegetable %r>' % self.vegname


class vegSchema(ma.SQLAlchemySchema):
    vegname = fields.Str(required = True, validate = Length(min=5))
    qty = fields.Integer(required = True, validate = Range(min=1))
    
    class Meta:
        fields = ("vegname","qty")

    
db.create_all()


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            
            current_user = User.query.filter_by(public_id=data['public_id']).first()
            print(current_user)
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user,*args,**kwargs)
    
    return wrapper


class register(Resource):
    def post(self):
        data = request.get_json()

        hashed_password = generate_password_hash(data['password'], method='sha256')

        new_user = User(public_id=str(uuid4()), name=data['name'],  password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'registered successfully'})


class login(Resource):
    def post(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

        user = User.query.filter_by(name=auth.username).first()

        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token': token})

        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})


'''
schema=vegSchema()
veg=vegetable(vegname='drumstick',qty=17)
db.session.add(veg)
db.session.commit()
print(vegetable.query.all())
print(schema.dump(veg))
'''

def abort_if_veg_doesnt_exist(name):
    if not vegetable.query.get(name):
          abort(400, "Veg doesn't exist")

schema=vegSchema(many=True)
schemaone=vegSchema()
class Vegetable(Resource):
    @token_required
    def get(self,current_user):
        veg=vegetable.query.all()
        result = schema.dump(veg)
        print(current_user)
        return result

    
    def post(self,current_user):
        error = schemaone.validate(request.json)
        if error:
            abort(400,str(error))
        vegname = request.json['vegname']
        qty = request.json['qty']
        veg=vegetable(vegname=vegname,qty=qty)
        db.session.add(veg)
        db.session.commit()
        return "Vegetable Added"


class Vegwitharg(Resource):
    @token_required
    def get(self,current_user,name):
        abort_if_veg_doesnt_exist(name)
        veg=vegetable.query.get(name)
        result = schemaone.dump(veg)
        return result

    def delete(self,name):
        abort_if_veg_doesnt_exist(name)
        veg=vegetable.query.get(name)
        db.session.delete(veg)
        db.session.commit()
        return "Vegetable Deleted"

    def put(self,name):
        abort_if_veg_doesnt_exist(name)
        veg=vegetable.query.get(name)
        veg.vegname=request.json['vegname']
        veg.qty=request.json['qty']
        db.session.commit()
        return "Vegetable updated"

api.add_resource(Vegetable,'/vegetables')
api.add_resource(Vegwitharg,'/vegetables/<string:name>')
api.add_resource(register,'/register')
api.add_resource(login,'/login')
