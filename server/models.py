from sqlalchemy import CheckConstraint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})


db=SQLAlchemy(metadata=metadata)

class User(db.Model,SerializerMixin):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, unique = True, nullable=False)
    password_hash=db.Column(db.String, nullable=False, )


class Guest(db.Model,SerializerMixin):
     __tablename__='guests'

     id=db.Column(db.Integer, primary_key=True)
     name=db.Column(db.String, nullable=False)
     occupation=db.Column(db.String, nullable=False)
     appearance=db.relationship('Appearance', back_populates='guest')

class Episode(db.Model,SerializerMixin):
     __tablename__='episodes'

     id=db.Column(db.Integer, primary_key=True)
     date=db.Column(db.Integer, nullable=False)
     number=db.Column(db.Integer, nullable=False)
     appearance=db.relationship('Appearance', back_populates='episode',cascade='delete all appearances')

class Appearance (db.Model,SerializerMixin):
      __tablename__='appearances'

      id=db.Column(db.Integer,primary_key=True)
      rating=db.Column(db.Integer)
      guest_id=db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
      episode_id=db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

      guest=db.relationship('Guest', back_populates='appearance')
      episode=db.relationship('Episode', back_populates='appearance')