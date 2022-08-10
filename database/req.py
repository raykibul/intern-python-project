import json
import ssl
from urllib.error import HTTPError
from urllib.request import Request, urlopen

global ctx

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get(url, headers={}):
    return send_req(url, 'GET', headers)


def post(url, headers={}):
    return send_req(url, 'POST', headers)


def put(url, headers={}):
    return send_req(url, 'PUT', headers)


def delete(url, headers={}):
    return send_req(url, 'DELETE', headers)


def send_req(url, method='GET', headers={}):
    req = Request(url=url, method=method)
    for key, value in headers.items():
        req.add_header(key, value)

    result = {'error': None}
    try:
        with urlopen(req, context=ctx) as res:
            body = res.read().decode('utf-8')
            result['body'] = json.loads(body)
            result['code'] = res.status
    except Exception as e:
        result['error']= e
        result['code'] = 422

    return result
