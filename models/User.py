# username': 'hisham', 'firstname': 'hasibul', 'lastname': 'hisham', 'id': '8', 'created_at': '2022-08-10T12:38:59.973349'
import json
from database.db import DB

class User(DB):

    def __init__(self, username, firstname, lastname,id=''):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.id = id


    def __str__(self):
        return f'username:{self.username},firstname:{self.firstname},lastname:{self.lastname},id:{self.id}'





