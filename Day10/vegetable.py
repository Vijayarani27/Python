from flask import Flask, request,abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api,Resource
from marshmallow import fields
from marshmallow.validate import Range, Length

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Vegetable.sqlite3'
api=Api(app)


db =SQLAlchemy(app)
ma = Marshmallow(app)

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
    def get(self):
        veg=vegetable.query.all()
        result = schema.dump(veg)
        print(result)
        return result


    def post(self):
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
    def get(self,name):
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

