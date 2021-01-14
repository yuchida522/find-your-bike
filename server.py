""" Server for Online Bike Exchange """
from flask import Flask, flash, redirect, render_template, request, session
from jinja2 import StrictUndefined
"""this will be there server file"""
import crud
from model import connect_to_db, db

app = Flask(__name__)
app.secret_key = "online_bike_exchange"
app.jinja_env.undefined = StrictUndefined

def server():
    pass

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True, port = 5002)