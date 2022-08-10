
import json
from database.db import DB
from database.db import DBModel


class User(DBModel):

    def __init__(self, username, firstname, lastname, id=''):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def __str__(self):
        return f'username:{self.username},firstname:{self.firstname},lastname:{self.lastname},id:{self.id}'
