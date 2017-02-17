import urllib
import http.cookiejar
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://200.200.169.212/server/index.php/mod_workreport'
postdata =urllib.parse.urlencode({
    "wrdate":1485878400000,
    "reportType":2,"opr":"create",
    "content":"55552222",
    "attrs":[]}
).encode('utf-8')
print(postdata)
header = {
    # 'Connection': 'keep-alive',
    # 'Content-Type': 'application/json',
    # 'Accept-Language': 'zh-CN,zh;q=0.8',
    # 'Accept': '*/*',
    # 'Origin': 'https://200.200.169.212',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
    # 'session-token': 'no-token',
    # 'X-Requested-With': 'XMLHttpRequest',
    # 'Referer': 'https://200.200.169.212/m/index.php',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Content-Length': 86,
    'Cookie':'sf_session=3lmkfjkianc4ooi0t1on22ei41',
    # 'Host': '200.200.169.212',
}
# header = {
# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
# "Accept-Encoding":"utf-8",
# "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
# "Connection":"keep-alive",
# "Host":"c.highpin.cn",
# "Referer":"http://c.highpin.cn/",
# "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
# }
req1 = urllib.request.Request(url,postdata,header)
req = urllib.request.urlopen(req1)
print(req.read().decode("utf8"))
# req = urllib.request.Request(url,postdata,header)
#
# print(urllib.request.urlopen(req).read().decode('utf-8'))
