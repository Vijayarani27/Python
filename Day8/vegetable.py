from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Vegetable.sqlite3'

db =SQLAlchemy(app)
ma = Marshmallow(app)

class vegetable(db.Model):
    vegname=db.Column(db.String(80), primary_key=True)
    qty=db.Column(db.Integer)

    def __repr__(self):
        return '<vegetable %r>' % self.vegname


class vegSchema(ma.SQLAlchemySchema):
    class Meta:
        model = vegetable

    vegname = ma.auto_field()
    qty = ma.auto_field()


db.create_all()
schema=vegSchema()
veg=vegetable(vegname='drumstick',qty=17)
db.session.add(veg)
db.session.commit()
print(vegetable.query.all())
print(schema.dump(veg))
