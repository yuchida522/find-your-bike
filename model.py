from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """table representing user"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement= True, primary_key = True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    phone_num = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    
    locations = db.relationship('Location')

    def __repr__(self):
        return f'<user_id= {self.user_id} fname= {self.fname} email= {self.email}>'

class Accessory(db.Model):
    """table representing posts other than bikes"""

    __tablename__= "accessories"

    accessory_id = db.Column(db.Integer, autoincrement= True, primary_key = True) 
    title = db.Column(db.String)
    description = db.Column(db.String)
    condition = db.Column(db.String)
    status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.listings_id'))

    status = db.relationship('Status')
    listings = db.relationship('listing')

    def __repr__(self):
        return f'<accessory id = {self.accessory_id}> title = {self.title} status id = {self.status_id}'


class Bicycle(db.Model):
    
    __tablename__ = 'bikes'

    bicycle_id = db.Column(db.Integer,
                           primary_key = True,
                           autoincrement=True)
    status_id = db.Column(db.Integer,
                          db.ForeignKey('status.status_id'),
                          nullable=False)
    listing_id = db.Column(db.Integer,
                           db.ForeignKey('listings.listing_id'),
                           nullable=False)

    height = db.Column(db.Integer, nullable=False)
    frame_type = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    bicycle_type = db.Column(db.String, nullable=False)
    condition = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False) #free or trade will be 0
    wheel_size = db.Column(db.Integer, nullable=False)
    handle_bar = db.Column(db.String(10), nullable=False)
    suspension = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)

    




class Post(db.Model):
    pass


class Location(db.Model):
    pass


class Photo (db.Model):
    """Stores photos for all user listings"""

    __tablename__ = "photos"


photo_id = db.Column(db.Integer, primary_key=True,
                     unique=True, autoincrement=True)
photo_url = db.Column(db.String(1000), nullable=False)

listings = db.relationship('Listing')


class Status (db.Model):
    """Keeps track of whether a bike is for sale, trade, or free"""

    __tablename__ = "status"


status_id = db.Column(db.Integer, primary_key=True,
                      unique=True, autoincrement=True)
sale = db.Column(db.String(1000), nullable=False)
trade = db.Column(db.String(1000), nullable=False)
free = db.Column(db.String(1000), nullable=False)

listings = db.relationship('Listing')
bicycles = db.relationship('Bicycle')
