import json
from models.User import User
from database.db import  DB

def main():
    db = DB()

    # url = "https://intern-test-server.herokuapp.com/api/users"
    # res = req.get(url=url, headers={'Content-Type': 'application/json'})
    user = User('Rakibul','MD.Rakibul','Islam')
    user.save()




if __name__ == '__main__':
    main()
