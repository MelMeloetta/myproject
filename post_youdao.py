import requests


url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
form_data={
'i': '我和你',
'from': 'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':'15847786751177',
'sign':'efcee979dd768aebfd1cb13e9befa70b',
'ts':'1584778675117',
'bv':'70244e0061db49a9ee62d341c5fed82a',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_CLICKBUTTION'
}
response=requests.post(url,data=form_data)
print(repsonse.text)