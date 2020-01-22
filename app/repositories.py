from app.models import Tweet


class TweetRepository():

    def __init__(self):
        self.tweets=[]
        self.compteur=0

    def add(self,tweet):
        self.compteur +=1
        tweet.set_id(self.compteur)
        self.tweets.append(tweet)

    def clear(self):
        self.tweets.clear()
        self.compteur=0

    def get(self,id):
        for tweet in self.tweets:
            if tweet.id == id :
                return tweet
        return None
