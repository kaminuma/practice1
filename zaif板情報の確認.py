import requests
from pprint import pprint

r = requests.get('https://api.zaif.jp/api/1/depth/zaif_jpy')
json = r.json()
pprint(json)