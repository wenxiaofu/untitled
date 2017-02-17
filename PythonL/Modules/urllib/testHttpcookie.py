import http.cookiejar
import urllib
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context
#使用cookie
cj = http.cookiejar.CookieJar()

#r = opener.open("http://www.baidu.com/")
# print(len(cj))
# for i in cj:
#     print(i)
#登陆
url='https://200.200.169.212/newim/'
postdata = b'{"reqtime":1466415752695,"nonce":"i0kmxSJF7lsq0uAeO9Kmj20yUoE=","srvtime":1466415755531,"action":"login","user":"12200000000","password":"12345"}'

print(postdata)

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
req= urllib.request.Request(url,postdata)
r = opener.open(req)
# r=urllib.request.urlopen(url,postdata)
# r = urllib.request.urlopen(url='https://200.200.169.212/newim/',
#                              data=b'{"reqtime":1466415752695,"nonce":"i0kmxSJF7lsq0uAeO9Kmj20yUoE=","srvtime":1466415755531,"action":"login","user":"12200000000","password":"12345"}')

print(r.read().decode("utf8"))
#提取需要的
tr=re.compile('"web_token":".*?",')
tr2=re.compile('"web_key":"(.+?)",')
tr3=re.compile('"websion":"(.+?)",')
str1=str(r.read().decode("utf8"))  #怕出错瞎弄了一个
web_token=re.findall("\"web_token\"\:\".*?\"\,",str1)
print(web_token)