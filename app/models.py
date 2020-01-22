import datetime

class Tweet():
    def __init__(self,message):

        self.text=message
        self.created_at= datetime.datetime.now()
        self.id = None

    def set_id(self,id):
        self.id=id

    def get_id(self):
        return self.id
