import hashlib
import hmac
import requests
import datetime
import urllib

#bitflyerのプライベートAPiリクエストを送信する関数
def bfPrivateApi(i_path, i_params=None):
    #API_KEY部分はBFから得た自分のAPIKEYを入力
    API_KEY = ("xxxxxxxxxxxxxxxxxxxx")
    #API_SECRET部分はBFから得た自分のPrivateKEYを入力
    API_SECRET = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    API_URL = ("http://api.bitflyer.jp")
    timestamp = str(datetime.datetime.today())
    headers = {'ACCESS-KEY':API_KEY, 'ACCESS-TIMESTAMP':timestamp,'Content-Type':'application/json'}
    s = hmac.new(bytearray(API_SECRET.encode('utf-8')),digestmod=hashlib.sha256)
    if i_params is None:
        w = timestamp + "GET" + i_path
        s.update(w.encode('utf-8'))
        headers['ACCESS-SIGN'] = s.hexdigest()
        return requests.get(API_URL + i_path, headers=headers)
    else:
        body = json.dumps(i_params);
        w = timestamp + "POST" + i_path + body
        s.update(w.encode('utf-8'))
        headers['ACCESS-SIGN'] = s.hexdigest()
        return requests.post(API_URL + i_path, data=body, headers=headers)
#プライベートAPIを使って自分の残高を確認する関数
b = bfPrivateApi("/v1/me/getbalance")
r = b.json()
print(r)

