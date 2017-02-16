import http.cookiejar
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'web.kd77.cn',
    'DNT': '1'
}
# postData={"reqtime":1466415752685,
#       "nonce":"i0kmxSJF7lsq0uAeO9Kmj20yUoE=",
#       "srvtime":1466415755531,
#       "action":"login",
#       "user":"23728632463",
#       "password":"12345"}
postData="{\"reqtime\":1466415752695,\"nonce\":\"i0kmxSJF7lsq0uAeO9Kmj20yUoE=\",\"srvtime\":1466415755531,\"action\":\"login\",\"user\":\"12200000000\",\"password\":\"12345\"}"
def getOpener(head):
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key,value in head.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders = header
    return opener
url="https://200.200.169.212/newim/"

# opener = getOpener(header)
# op = opener.open(url)
# print(op.read().decode("utf8"))
postData = urllib.parse.urlencode(postData).encode()
print(postData)
# op = opener.open(url, postData)
# op = opener.open(url, postData)
op = urllib.request.urlopen(url,postData)
data = op.read()
print(data.decode("utf8"))