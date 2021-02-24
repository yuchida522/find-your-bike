from model import db, User,  Accessory, Bicycle, Photo, Status, Location, Listing, Comment, connect_to_db
from datetime import datetime


def create_user(fname, lname, email, phone_num, created_at):
    """Create and add user to the db"""
    user = User(fname=fname, lname=lname, email=email, phone_num=phone_num,
                 created_at=created_at)

    db.session.add(user)
    db.session.commit()

    return user


def create_accessory(title, description, condition, price, status_id, listing_id, user_id):
    """Create and add accessories to the bd based on lisitng and user"""
    accessories = Accessory(title=title, description=description, condition=condition,
                            price=price, status_id = status_id, listing_id = listing_id, user_id = user_id)

    db.session.add(accessories)
    db.session.commit()

    return accessories


def create_listing(created_at, title, listing_user_id,listing_status_id, flagged=False):
    """Create and return a listing """
    listing = Listing(created_at=created_at, title=title,
                      listing_user_id=listing_user_id,listing_status_id = listing_status_id, flagged=flagged)

    db.session.add(listing)
    db.session.commit()

    return listing


def create_comment(listing_id, user_id, comment_text):
    """ Create and return a comment"""
    comment = Comment(listing_id=listing_id, user_id=user_id,
                      comment_text=comment_text)

    db.session.add(comment)
    db.session.commit()

    return comment


def create_bicycle(status_id, listing_id, user_id, frame_size, frame_type, brand, model, bicycle_type,
                condition, price, description):
    """creates a bike and saves into db"""

    bicycle = Bicycle(status_id=status_id,
                      listing_id=listing_id,
                      user_id=user_id,
                      frame_size=frame_size,
                      frame_type=frame_type,
                      brand=brand,
                      model=model,
                      bicycle_type=bicycle_type,
                      condition=condition,
                      price=price,
                      description=description)

    db.session.add(bicycle)
    db.session.commit()

    return bicycle


def create_location(name, zipcode, longitude, latitude,user_id):
    """creates location and saves into db"""

    location = Location(name = name,
                        zipcode=zipcode,
                        longitude=longitude,
                        latitude=latitude,
                        user_id = user_id)

    db.session.add(location)
    db.session.commit()

    return location


# def create_status(sale, trade, free, status_listing_id, status_bicycle_id):
def create_status(status_name):
    """Create and return status of bicycle for a listing"""
    status = Status(status_name = status_name )
    db.session.add(status)
    db.session.commit()
    # status = Status(sale=sale, trade=trade, free=free,
    #                 status_listing_id=status_listing_id, status_bicycle_id=status_bicycle_id)
    

    

    return status


def create_photo(photo_url, photo_listing_id):
    """Create and return listing photos"""

    photos = Photo(photo_url=photo_url, photo_listing_id=photo_listing_id)

    db.session.add(photos)
    db.session.commit()

    return photos

def get_user_by_email(email):

    user_email = User.query.filter(User.email == email).first()

    return user_email

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
