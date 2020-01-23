from flask_testing import TestCase
from app import create_app, db
from app.models import Tweet


class TestTweetViews(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = f"{app.config['SQLALCHEMY_DATABASE_URI']}_test"
        return app

    def setUp(self):
        db.create_all()
        first_tweet = Tweet(text="First tweet")
        db.session.add(first_tweet)
        db.session.commit()
        second_tweet = Tweet(text="Secound tweet")
        db.session.add(second_tweet)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_tweet_create_KO_nodata(self):
        response = self.client.post("/tweets")
        self.assertEqual(response.status_code, 422)



