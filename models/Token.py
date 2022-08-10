from database.db import DB, DBModel


class Token(DBModel):

    def __init__(self, id, token=None, refresh=None):
        self.id = id
        self.token = token
        self.refresh = refresh
