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

# class Bike(db.Model):
#     pass

# class Post(db.Model):
#     pass

# class Location(db.Model):
#     pass