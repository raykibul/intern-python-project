import json
from models.User import User
from models.Token import Token
from models.Tweet import Tweet
from database.db import  DB
from pyjokes import get_joke
from utils import Utitls
import time
import getpass





db = DB()
util= Utitls()
#check if refresh token existed or not

res = util.get_existing_token()


if res == None:
    print('no saved token found . please log in .. ')
    username = input('Username: ')
    password =  getpass.getpass('Password:')
    new_token_res = util.obtain_token(username,password)['body']
    token = Token(1,new_token_res['access_token'],new_token_res['refresh_token'])
    token.save()
else:
    token = Token(res[0], res[1], res[2])
print(token.token)



#if not obtain token by using username password

#if token existed parse

#util.obtain_token('rakibul','123456')

print(get_joke())

