from model import db, User,  Accessory, Bicycle, Photo, Status, Location, Listing, Comment, connect_to_db
from datetime import datetime

def create_user(fname, lname, email, phone_num, created_at, location_id):
    """Create and add user to the db"""
    users = User(fname=fname, lname=lname, email=email, phone_num=phone_num, created_at=created_at, location_id=location_id)

    db.session.add(users)
    db.session.commit()

    return users

def create_accessory(title, description, condition, price, status_id, listing_id):
    """Create and add accessories to the bd based on lisitng and user"""
    accessories = Accessory(title=title, description=description, condition=condition, price=price, status_id=status_id, listing_id=listing_id)

    db.session.add(accessories)
    db.session.commit()

    return accessories


def create_listing(created_at,title,listing_user_id,flagged = False):
    """Create and return a listing """
    listing = Listing(created_at = created_at, title = title, listing_user_id = listing_user_id,flagged = flagged )
    
    db.session.add(listing)
    db.session.commit()

    return listing


def create_comment(listing_id,user_id,comment_text):
    """ Create and return a comment"""
    comment = Comment(listing_id = listing_id, user_id = user_id, comment_text = comment_text )

    db.session.add(listing)
    db.session.commit()

    return comment

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
