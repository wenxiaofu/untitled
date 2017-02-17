import urllib
import http.cookiejar
import ssl
#实现登陆

#正则提取web_token

#获取cookie进行业务请求


#http://www.cnblogs.com/zl0372/p/5486683.html
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
    # 'X-Requested-With': 'XMLHttpRequest',#没有这个表示是传统请求，会返回整个页面，有这个表示是ajax请求，只返回部分
    'Referer': 'https://200.200.169.212/m/index.php',
    # 'Accept-Encoding': 'gzip, deflate',
    #'Content-Length': 86,
    # 'Cookie':'sf_session=3lmkfjkianc4ooi0t1on22ei41',
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
# req = urllib.request.urlopen(req1)
# print(req.read().decode("utf8"))
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(req1)
print(r.read().decode('utf-8'))
r.close()
cj.make_cookies('name','value')

print("----------")
print(len(cj))
# print(cj.value)
print(cj._cookies_for_domain("200.200.169.212",r))

cj.clear()
for item in cj:
    print("----------")
    print(item)


'''
说明：带cookie的打印出来必须用opener.open(req).read().decode('utf-8')
来发送的请求才会带上cookie，如果用urllib.request.urlopen()
是不带cookie的

说明：
1.
urllib.request.Request()
返回了一个request的请求实例
2.
urlopen是一个封装好的OpenerDirector实例，里面只有三个参数（url，data，timeout）
3.
通过build_opener可以自己创建一个OpenerDirector实例，所以如果想要构建一个cookie管理
build_opener(*handlers)，将handler类实例化增加到OpenerDirector中，比如像上面的例子里增加cookie，
# req = urllib.request.Request(url,postdata,header)
#
# print(urllib.request.urlopen(req).read().decode('utf-8'))
'''