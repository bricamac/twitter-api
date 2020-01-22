# app/__init.py__
from flask import Flask
from flask_restplus import Api

#Init base...
from app.models import Tweet
from app.db import tweet_repository
first_tweet = Tweet("1er tweet")
tweet_repository.add(first_tweet)
first_tweet = Tweet("2eme tweet")
tweet_repository.add(first_tweet)

def create_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return "Goodbye World!"

    from .apis.tweets import api as tweets
    api = Api()
    api.add_namespace(tweets)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False

    return app
