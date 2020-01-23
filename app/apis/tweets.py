from flask_restplus import Namespace, Resource, fields
from app import db
from app.models import Tweet

api = Namespace('tweets')

tweet_model = api.model('Tweet', {
    'id': fields.Integer(readonly=True, description='The tweet unique identifier'),
    'text': fields.String(required=True, description='The tweet details'),
    'created_at': fields.Date(required=True, description='The tweet details')
})

tweet_model_lite = api.model('Tweet', {
    'text': fields.String(required=True, description='The tweet details'),
})

@api.route('/')
class TweetResourceRacine(Resource):
    @api.doc('create_todo')
    @api.expect(tweet_model)
    @api.marshal_with(tweet_model_lite, code=201)
    def post(self):
        if api.payload is None:
            api.abort(422,'{"error": "input data error""}')

        #tweet=Tweet(text=data["text"])
        #db.session.add(tweet)
        #db.session.commit()
        return api.payload,201

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
@api.param('id', 'The tweet unique identifier')
class TweetResource(Resource):
    #Lecteur un tweet
    @api.doc('get tweet')
    @api.marshal_with(tweet_model)
    def get(self, id):
        tweet = db.session.query(Tweet).get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet

    #Suppression
    def delete(self,id):
        tweet = db.session.query(Tweet).get(id)
        if tweet is None:
            api.abort(404)

        db.session.delete(tweet)
        try:
            db.session.commit()
            return "", 204
        except:
            api.abort(500,'{"error":"Database"}')

