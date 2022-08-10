from database import req
import time
from models.Token import Token

class Utitls():
    def __init__(self):
        self.main_url = "https://intern-test-server.herokuapp.com"
        self.login_url = self.main_url+"/api/auth"

    def log_time(fn):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            ans = fn(*args, **kwargs)
            end_time = time.time()
            print("elapsed time : ", end_time - start_time)
            return ans
        return wrapper

    @log_time
    def obtain_token(self,username,password):
        data = {
            'username':username,
            'password':password
        }
        res = req.post(self.login_url, headers={'Content-Type': 'application/json'},data=data)
        return res

    @log_time
    def get_existing_token(self):
        token = Token(1)
        return token.get_one(1)



