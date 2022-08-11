from database import req
import time
from models.Token import Token


class Utitls():
    def __init__(self):
        self.main_url = "https://intern-test-server.herokuapp.com"
        self.login_url = self.main_url + "/api/auth"
        self.refresh_url = self.main_url + "/api/auth/token"
        self.tweets_url = self.main_url + "/api/tweets"


    def log_time(fn):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            ans = fn(*args, **kwargs)
            end_time = time.time()
            print("elapsed time : ", end_time - start_time)
            return ans

        return wrapper

    @log_time
    def obtain_token(self, username, password):
        data = {
            'username': username,
            'password': password
        }
        res = req.post(self.login_url, headers={'Content-Type': 'application/json'}, data=data)
        return res

    @log_time
    def get_existing_token(self):
        token = Token(1)
        return token.get_one(1)

    def token_refresh(self, refresh_token):
        print('refresing existing token')
        data = {
            'refresh_token': refresh_token
        }
        res = req.post(self.refresh_url, headers={'Content-Type': 'application/json'}, data=data)
        res = res['body']
        token = Token(1, res['access_token'], res['refresh_token'])
        token.save()
        return token

    @log_time
    def get_tweets(self, token):
        data = {
            'limit': 5
        }
        headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {token}"
        }

        res = req.get(self.tweets_url, headers=headers, data=data)
        return res

    @log_time
    def post_tweet(self, tweet, token):
        data = {
            'text': tweet
        }
        headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {token}"
        }
        res = req.post(self.tweets_url, headers=headers, data=data)
        print(res)
        return res