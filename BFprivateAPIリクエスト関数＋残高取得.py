import hashlib
import hmac
import requests
import datetime
import urllib

#bitflyer�̃v���C�x�[�gAPi���N�G�X�g�𑗐M����֐�
def bfPrivateApi(i_path, i_params=None):
    #API_KEY������BF���瓾��������APIKEY�����
    API_KEY = ("xxxxxxxxxxxxxxxxxxxx")
    #API_SECRET������BF���瓾��������PrivateKEY�����
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
#�v���C�x�[�gAPI���g���Ď����̎c�����m�F����֐�
b = bfPrivateApi("/v1/me/getbalance")
r = b.json()
print(r)

