from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """table representing user"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
        autoincrement=True, 
        primary_key=True)
    fname = db.Column(db.String, nullable = False)
    lname = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullabe = False)
    phone_num = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, nullable = True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))

    user_location = db.relationship('Location')

    def __repr__(self):
        return f'<user_id= {self.user_id} || fname= {self.fname} || email= {self.email}>'


class Accessory(db.Model):
    """table representing posts other than bikes"""

    __tablename__ = "accessories"

    accessory_id = db.Column(db.Integer, 
        autoincrement=True, 
        primary_key=True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String(3000), nullable = False)
    condition = db.Column(db.String(25), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.listing_id'))

    accessory_status = db.relationship('Status')
    accessory_listing = db.relationship('Listing')

    def __repr__(self):
        return f'<accessory id = {self.accessory_id}> || title = {self.title} || status id = {self.status_id}'


class Bicycle(db.Model):
    """table representing a bike"""

    __tablename__ = 'bikes'

    bicycle_id = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True)
    status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.listing_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    height = db.Column(db.Integer, nullable=False)
    frame_type = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    bicycle_type = db.Column(db.String, nullable=False)
    condition = db.Column(db.String(25), nullable=False)
    price = db.Column(db.Integer, nullable=False)  # free or trade will be 0
    wheel_size = db.Column(db.Integer, nullable=False)
    handle_bar = db.Column(db.String(20), nullable=False)
    suspension = db.Column(db.String, nullable=False)
    description = db.Column(db.Text(3000), nullable=False)

    bicycle_status = db.relationship('Status')
    bicycle_listing = db.relationship('Listing')
    bicycle_user = db.relationship('User')

    def __repr__(self):
        return f'<Bicycle bicycle_id={self.bicycle_id} || user_id={self.user_id}>'



class Photo (db.Model):
    """Stores photos for all user listings"""

    __tablename__ = "photos"

    photo_id = db.Column(db.Integer,
                         primary_key=True,
                         unique=True,
                         autoincrement=True)
    photo_url = db.Column(db.String(1000), nullable=False)
    photo_listing_id = db.Column(db.Integer,
                                 db.ForeignKey('listings.listing_id'))

    photo_listing = db.relationship('Listing')

    def __repr__(self):
        return f'< photo_id = {self.photo_id} || photo_url = {self.photo_url} >'


class Status (db.Model):
    """Keeps track of whether a bike is for sale, trade, or free"""

    __tablename__ = "status"

    status_id = db.Column(db.Integer,
                          primary_key=True,
                          unique=True,
                          autoincrement=True)
    sale = db.Column(db.Boolean, nullable=False)
    trade = db.Column(db.Boolean, nullable=False)
    free = db.Column(db.Boolean, nullable=False)
    status_listing_id = db.Column(db.Integer,
                                  db.ForeignKey('listings.listing_id'))
    status_bicycle_id = db.Column(db.Integer,
                                  db.ForeignKey('bicycles.bicycle_id'))

    status_listing = db.relationship('Listing')
    status_bicycle = db.relationship('Bicycle')

    def __repr__(self):
        return f'< Status = {self.status_id} || sale = {self.sale} || trade = {self.trade} free = {self.free} >'


class Location(db.Model):
    """ Location of the user """
    __tablename__ = 'locations'

    location_id = db.Column(db.Integer,
                            primary_key=True,
                            autoincrement=True)
    zipcode = db.Column(db.Integer, nullable = False)
    longitude = db.Column(db.Float, nullable = False)
    latitude = db.Column(db.Float, nullable = False)

    user_location = db.relationship("User")

    def __repr__(self):
        return f'< Location location_id = {self.location_id}|| zipcode = {self.zipcode} || longitude = {self.longitude} || latitude = {self.latitude} >'


class Listing(db.Model):
    """ Listing created by a user """
    __tablename__ = 'listings'

    listing_id = db.Column(db.Integer,
                        primary_key = True, 
                        autoincrement = True)
    created_at = db.Column(db.DateTime, nullable = False)
    title = db.Column(db.String(100), nullable = False)
    listing_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    flagged = db.Column(db.Boolean, default= False, nullable = False)

    bicycle_listing = db.relationship("Bicycle")
    photo_listing = db.relationship("Photo")
    comment_listing = db.relationship("Comment")
    accessories_listing = db.relationship("Accessory")
    user_listing = db.relationship("User")

    def __repr__(self):
        return f'< Listing listing_id = {self.listing_id}|| created_at = {self.created_at} || title = {self.title} || listing_user_id = {self.listing_user_id} || flagged = {self.flagged} >'


class Comment(db.Model):
    """Comments for a post """
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer,
                        primary_key = True, 
                        autoincrement = True)
    listing_id = db.Column(db.Integer,db.ForeignKey('listings.listing_id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    comment_text = db.Column(db.Text, nullable = False)

    comment_listing = db.relationship("Listing")
    comment_user = db.relationship("User")

    def __repr__(self):
        return f'< Comment comment_id = {self.comment_id}|| listing_id = {self.listing_id} || user_id = {self.user_id} >'
