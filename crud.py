<<<<<<< HEAD
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


def create_bike(status_id, listing_id, user_id, height, frame_type, brand, model, bicycle_type, 
                condition, price, wheel_size, handle_bar, suspension, description):
    """creates a bike and saves into db"""
    
    bicycle = Bicycle(status_id=status_id,
                      listing_id=listing_id,
                      user_id=user_id,
                      height=height,
                      frame_type=frame_type,
                      brand=brand,
                      model=model,
                      bicycle_type=bicycle_type,
                      condition=condition,
                      price=price,
                      wheel_size=wheel_size,
                      handle_bar=handle_bar,
                      suspension=suspension,
                      description=description)

    db.session.add(bicycle)
    db.session.commit()

    return bicycle

def create_location(zipocde, longitude, latitude):
    """creates location and saves into db"""

    location = Location(zipcode=zipcode,
                        longitude=longitude,
                        latitude=latitude)

    db.session.add(location)
    db.session.commit()

    return location


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
=======


def create_status(sale, trade, free, status_listing_id, status_bicycle_id):
    """Create and return status of bicycle for a listing"""

    status = Status(sale=sale, trade=trade, free=free,
                    status_listing_id=status_listing_id, status_bicycle_id=status_bicycle_id)

    db.session.add(status)
    db.session.commit()

    return status


def create_photo(photo_url, photo_listing_id):
    """Create and return listing photos"""

    photos = Photo(photo_url=photo_url, photo_listing_id=photo_listing_id)

    db.session.add(photos)
    db.session.commit()

    return photos
>>>>>>> aab79f4... add crud functions for Photo and Status
