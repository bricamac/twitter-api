from flask_restplus import Namespace, Resource, fields
from app.db import tweet_repository

api = Namespace('tweets')

tweet_model = api.model('Tweet', {
    'id': fields.Integer(readonly=True, description='The tweet unique identifier'),
    'text': fields.String(required=True, description='The tweet details'),
    'created_at': fields.Date(required=True, description='The tweet details')
})

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
@api.param('id', 'The tweet unique identifier')
class TweetResource(Resource):
    @api.doc('get tweet')
    @api.marshal_with(tweet_model)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet
