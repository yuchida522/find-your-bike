from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """table representing user"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
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

    __tablename__ = "accessories"

    accessory_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
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
                           primary_key=True,
                           autoincrement=True)
    status_id = db.Column(db.Integer,
                          db.ForeignKey('status.status_id'),
                          nullable=False)
    listing_id = db.Column(db.Integer,
                           db.ForeignKey('listings.listing_id'),
                           nullable=False)
    user_id = db.Coluimn(db.Integer,
                         db.ForeignKey('users.user_id'),
                         nullable=False)
    height = db.Column(db.Integer, nullable=False)
    frame_type = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    bicycle_type = db.Column(db.String, nullable=False)
    condition = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)  # free or trade will be 0
    wheel_size = db.Column(db.Integer, nullable=False)
    handle_bar = db.Column(db.String(10), nullable=False)
    suspension = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)

    status = db.relationship('Status')
    listing = db.relationship('Listing')
    user = db.relationship('User')

    def __repr__(self):
        return f'<Bicycle bicycle_id={self.bicycle_id}, user_id={self.user_id}>'


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

    def __repr__(self):
        return f'< photo_id = {self.photo_id}, photo_url = {self.photo_url} >'


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

    def __repr__(self):
        return f'< Status = {self.status_id}>'


class Location(db.Model):
    """ Location of the user """
    __tablename__ = 'locations'

    location_id = db.Column(db.Integer,
                            primary_key=True,
                            autoincrement=True)
    zipcode = db.Column(db.Integer)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    user_locations = db.relationship("User")

    def __repr__(self):
        return f'< Location location_id = {self.location_id}|| zipcode = {self.zipcode} || longitude = {self.longitude} || latitude = {self.latitude} >'


class Listing(db.Model):
    """ Listing created by a user """
    __tablename__ = 'listings'

    listing_id int = db.Column(db.Integer,
                               primary_key=True,
                               autoincrement=True)
    created_at = db.Column(db.DateTime)
    title = db.Column(db.String(100))
    listing_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    flagged = db.Column(db.Boolean)

    bicycle_listings = db.relationship("Bicycle")
    photo_listings = db.relationship("Photo")
    comment_listings = db.relationship("Comment")
    accessories_listings = db.relationship("Accessories")

    user_listing = db.relationship("User")

    def __repr__(self):
        return f'< Listing listing_id = {self.listing_id}|| created_at = {self.created_at} || title = {self.title} || listing_user_id = {self.listing_user_id} || flagged = {self.flagged} >'


class Comment(db.Model):
    """Comments for a post """
    __tablename__ = 'comments'

    comment_id int = db.Column(db.Integer,
                               primary_key=True,
                               autoincrement=True)
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.listing_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    comment_text = db.Column(db.Text)

    comment_listing = db.relationship("Listing")
    comment_user = db.relationship("User")

    def __repr__(self):
        return f'< Comment comment_id = {self.comment_id}|| listing_id = {self.listing_id} || user_id = {self.user_id} >'
