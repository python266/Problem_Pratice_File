import requests as rq

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
data = {"somekey": "somewhere"}
d = rq.post(url=url, json=data)
print(d.text)