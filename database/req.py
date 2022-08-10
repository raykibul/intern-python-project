import json
import ssl
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from urllib import parse

global ctx

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get(url, headers={},data={}):
    return send_req(url, 'GET', headers,data)


def post(url, headers={},data={}):
    return send_req(url, 'POST', headers,data)


def put(url, headers={},data={}):
    return send_req(url, 'PUT', headers,data={})


def delete(url, headers={},data={}):
    return send_req(url, 'DELETE', headers,data={})


def send_req(url, method='GET', headers={}, data={}):
    req = Request(url=url, method=method)
    for key, value in headers.items():
        req.add_header(key, value)
    result = {'error': None}
    try:
        data =  bytes(json.dumps(data,indent=4),"utf-8")
        with urlopen(req, context=ctx, data=data) as res:

            body = res.read().decode('utf-8')
            result['body'] = json.loads(body)
            result['code'] = res.status
    except Exception as e:
        result['error'] = e
        result['code'] = 422

    return result
