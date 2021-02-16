import os
from random import choice, randint
from datetime import datetime
from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db, User, Accessory, Bicycle, Photo, Status, Location, Listing, Comment
import crud
from server import app
import csv


os.system('dropdb bike')	
status = os.system('createdb bike')
print(status)

connect_to_db(app)
db.create_all()


def open_pipe_file(pipe_file):
    with open(pipe_file ,'r') as open_file:
        result_list = []

        for line in open_file:
            result_list.append(line.rstrip().split('|'))

        return result_list

user_file = open_pipe_file("seed_data/user.csv")
for user in user_file:
    created_at,location_id, fname, lname, phone_num, email = user
    all_user = crud.create_user(fname, lname, email, phone_num, created_at)

status_name = ['sale','trade','free']
for status in status_name:
    all_status = crud.create_status(status)

listing_file = open_pipe_file("seed_data/listing.csv")
print("lsiting file is:",listing_file)
for listing in listing_file:
    listing_status_id = choice([1,2,3])
    created_at, title, listing_user_id, flagged = listing
    all_listing = crud.create_listing(created_at, title, listing_user_id,listing_status_id, flagged)


accessory_file = open_pipe_file("seed_data/accessories.csv")
for acc in accessory_file:
    title, description, condition, price, id_num  = acc
    status_id = choice([1,2,3])
    # setting listing_id, user_id as id_num value
    all_acc = crud.create_accessory(title, description, condition, price, status_id, id_num, id_num) 


bicycle_file = open_pipe_file("seed_data/bicycle.csv")
for bicycle in bicycle_file:
    status_id = choice([1,2,3])
    id_num, frame_size, frame_type, brand, model, bicycle_type, condition, price, description = bicycle
    # setting listing_id, user_id as id_num value
    all_bicycle = crud.create_bicycle(status_id, id_num, id_num, frame_size, frame_type, brand, model, bicycle_type,
                condition, price, description)


photo_file = open_pipe_file("seed_data/photo_seed.csv")
for photo in photo_file:
    photo_url, photo_listing_id = photo
    all_photo = crud.create_photo(photo_url, photo_listing_id)


location_file = open_pipe_file("seed_data/location_seed.csv")
for location in location_file:
    name,zipocde, longitude, latitude, user_id = location
    all_location = crud.create_location(name,zipocde, longitude, latitude , user_id)


comment_file = open_pipe_file("seed_data/comment.csv")
for comment in comment_file:
    listing_id, user_id, comment_text =  comment
    all_comment = crud.create_comment(listing_id, user_id, comment_text)