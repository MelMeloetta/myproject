import random
import requests
import time

from requests import Response

# url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# content='好坏'

class Youdao():
    def __init__(self,content):
        self.content=content
        self.url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()

    def get_salt(self):
        s=str(random.randint(0,10))
        t=self.ts
        return t+s

    def get_md5(self,value):
        import hashlib
        m=hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        i=self.salt
        e=self.content
        s="fanyideskweb"+e+i+"Nw(nmmbP%A-r6U3EUn]Aj"
        print("s=", self.get_md5(s))
        return self.get_md5(s)


    def get_ts(self):
        t = time.time()
        ts = str(int(round(t * 1000)))
        print('ts=',ts)
        return ts



    def yield_form_data(self):
        form_data = {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'sign': self.sign,
            'salt': self.salt,

            'ts': self.ts,
            'bv': '70244e0061db49a9ee62d341c5fed82a',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return form_data

    def get_headers(self):
        headers={
            'Cookie': 'OUTFOX_SEARCH_USER_ID=1515049784@101.65.62.209; OUTFOX_SEARCH_USER_ID_NCOO=467837354.75629026; UM_distinctid=170d1f6a756ba9-05efd50b41dbef-4313f6a-1fa400-170d1f6a757c98; _ntes_nnid=32040b45048f55fcb306fb93229c5210,1585531105140; JSESSIONID=aaaAz71hcWBR9alvYKIfx; ___rl__test__cookies=1586500510256',
            'Referer': 'http: // fanyi.youdao.com /',
            'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        }
        return headers


    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        return response.text


if __name__ =="__main__":
    youdao=Youdao('牛鼻')
    print(youdao.fanyi())
