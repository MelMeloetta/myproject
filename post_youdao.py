import random
import requests
import time

url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    return t+s

def get_sign():
    return "308b3838d4426879f828b90a600357d6"

def get_ts():
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts



form_data={
'i':'好坏',
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':'15856147553208',
'sign':'308b3838d4426879f828b90a600357d6',
'ts':'1585614755320',
'bv':'70244e0061db49a9ee62d341c5fed82a',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTlME',
}
response=requests.post(url,data=form_data)
print(response.text)