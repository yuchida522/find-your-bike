from model import db, User,  Accessory, Bicycle, Photo, Status, Location, Listing, Comment connect_to_db
from datetime import datetime

def create_user(fname, lname, email, phone_num, created_at, location_id):
    """Create and add user to the db"""
    users = User(fname=fname, lname-lname, email=email, phone_num=phone_num, created_at=created_at, location_id=location_id)

    db.session.add(users)
    db.session.commit()

    return users

dec create_accessory(title, description, condition, price, status_id, listing_id):
    """Create and add accessories to the bd based on lisitng and user"""
    accessories = Accessory(title=title, description=description, condition=condition, price=price, status_id=status_id, listing_id=listing_id)

    db.session.add(accessories)
    db.session.commit()

    return accessories