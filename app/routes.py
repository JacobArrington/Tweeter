from app import app, tweets
from flask import render_template
from app.tweets import tweets
from random import choice


@app.route('/')
def index():

    ran_tweet = choice(tweets)

    return render_template('index.html', tweet=ran_tweet)


@app.route('/feed')
def feed():
    return render_template('feed.html',tweets=tweets)
