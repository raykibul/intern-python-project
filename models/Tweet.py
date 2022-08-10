from database.db import DBModel
from models.User import User
from datetime import datetime


class Tweet(DBModel):

    def __init__(self, id, text, author, created_at='', updated_at=''):
        self.id = id
        self.text = text
        self.author = author
        self.create_at = created_at
        self.updated_at = updated_at
