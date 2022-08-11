import json
from models.User import User
from models.Token import Token
from models.Tweet import Tweet
from database.db import DB
from pyjokes import get_joke
from utils import Utitls
import time
import getpass

db = DB()
util = Utitls()

# check if refresh token existed in db or not

res = util.get_existing_token()
token = None

if res == None:
    print('no saved token found . please log in .. ')
    username = input('Username: ')
    password = getpass.getpass('Password:')
    new_token_res = util.obtain_token(username, password)['body']
    token = Token(1, new_token_res['access_token'], new_token_res['refresh_token'])
    token.save()
else:
    print('User token exist!')
    token = Token(res[0], res[1], res[2])

# fetching last 5 tweets
tweet_res = util.get_tweets(token.token)
print('fetching tweets using existing token')
if tweet_res['code'] == 422:
    print('token expired! trying to get new token using refresh token')
    token = util.token_refresh(token.refresh)
    tweet_res = util.get_tweets(token.token)

##
for item in tweet_res['body']:
    author = item['author']
    id = item['id']
    created_at = item['created_at']
    text = item['text']
    print(f"({id}) {author['username']} tweeted at {created_at} ")
    print(f"{text}")

print('generating 10 unique jokes ')

jokes = set()
while len(jokes) < 10:
    jokes.add(get_joke())
print(jokes)

for joke in jokes:
    print('tweeting a new joke')
    res = util.post_tweet(joke, token.token)
    if res['code'] == 422:
        token = util.token_refresh(token.refresh)
    time.sleep(60)
