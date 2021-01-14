import os
from random import choice, randint
from datetime import datetime
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db, db, User, Accessory, Bicycle, Photo, Status, Location, Listing, Comment
import crud
from server import app

connect_to_db(app)
db.create_all()


