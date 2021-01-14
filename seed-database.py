import os
from random import choice, randint
from datetime import datetime
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db, User, Accessory, Bicycle, Photo, Status, Location, Listing, Comment
import crud
from server import app

connect_to_db(app)
db.create_all()

def open_pipe_file():
    with(pipe_file) as open_file:
        result_list = []

        for line in open_file:
            result_list.append(line.rstrip().split('|'))

        return result 

user_file = open_pipe_file("seed_data/user.csv")
for user in user_file:
    fname, lname, email, phone_num, created_at, location_id = user
    all_user = crud.create_user(fname, lname, email, phone_num, created_at, location_id)

accessory_file = open_pipe_file("seed_data/accessories.csv")
for acc in accessory_file:
    title, description, condition, price, status_id, listing_id  = acc
    all_acc = crud.create_accessory(title, description, condition, price, status_id, listing_id)


