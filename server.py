""" Server for Online Bike Exchange """
from model import connect_to_db, db
from flask import Flask, flash, redirect, render_template, request, session
from jinja2 import StrictUndefined
import os
import secrets

# from algoliasearch.search_client import SearchClient
"""this will be there server file"""
# import crud

app = Flask(__name__)
app.secret_key = "online_bike_exchange"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():

    return render_template('base.html')


@app.route('/about')
def about():

    return render_template('base.html')


@app.route('/login')
def login():

    return render_template('base.html')


@app.route('/profile')
def profile():

    return render_template('base.html')


############ ALGOLIA ###############


# client = SearchClient.create(
#     os.environ['ALGOLIA_API_ID'],
#     os.environ['ALGOLIA_API_KEY']
# )

# index = client.init_index('testing')

# # Enid testing:
# index.save_objects([{"objectID": 8, "brand": "test8"}])

# Enid testing:
# objects = index.search('test')


if __name__ == '__main__':
    connect_to_db(app)
    # only this host number works for Yuri, look into why
    app.run(host='127.0.0.1', debug=True, port=5002)

    # app.run(host='0.0.0.0', debug=True, port = 5002)
