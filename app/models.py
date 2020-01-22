import datetime

class Counter:
    def __init__(self):
        self.id = 1

    def next(self):
        self.id += 1
        return self.id
class Tweet():
    tweet_counter=Counter()
    def __init__(self,message):

        self.text=message
        self.created_at= datetime.datetime.now()
        self.id = None
