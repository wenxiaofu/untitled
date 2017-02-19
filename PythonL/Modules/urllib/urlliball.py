'''
这一个文档主要用来学习urllib


'''
#例子用来登录csdn官网

import urllib
from urllib import request
url = 'https://passport.csdn.net/account/login?ref=toolbar'
postdata=b'username=695144224%40qq.com&password=444&lt=LT-742536-9fTYjvtSYonjSIjIxzWhcGccOavImk&execution=e5s2&_eventId=submit'
header = {
    # 'Connection': 'keep-alive',
    # 'Content-Type': 'application/json',
    # 'Accept-Language': 'zh-CN,zh;q=0.8',
    # 'Accept': '*/*',
    # 'Origin': 'https://200.200.169.212',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
    # 'session-token': 'no-token',
    'X-Requested-With': 'XMLHttpRequest',#没有这个表示是传统请求，会返回整个页面，有这个表示是ajax请求，只返回部分
    'Referer': 'https://200.200.169.212/m/index.php',
    # 'Accept-Encoding': 'gzip, deflate',
    #'Content-Length': 86,
    # 'Cookie':'sf_session=3lmkfjkianc4ooi0t1on22ei41',
    # 'Host': '200.200.169.212',
}
#直接调用urlopen
with urllib.request.urlopen(url,postdata) as f : print(f.read().decode("utf8"))



