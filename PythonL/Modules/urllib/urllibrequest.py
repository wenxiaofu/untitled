import urllib.request
import ssl
import http.cookiejar
ssl._create_default_https_context = ssl._create_unverified_context

req = urllib.request.Request(url='https://200.200.169.212/newim/',
                             data=b'{"reqtime":1466415752695,"nonce":"i0kmxSJF7lsq0uAeO9Kmj20yUoE=","srvtime":1466415755531,"action":"login","user":"12200000000","password":"12345"}')

with urllib.request.urlopen(req) as f:print(f.read().decode('utf-8'))
#add header
head = {
    'Referer', 'http://200.200.169.212/',
    'Content-Type', 'application/json',
}
cj = http.cookiejar.CookieJar()
cj.add_cookie_header('sf_session=3lmkfjkianc4ooi0t1on22ei41')
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open('https://200.200.169.212/newim/',
                data=b'{"reqtime":1466415752695,"nonce":"i0kmxSJF7lsq0uAeO9Kmj20yUoE=","srvtime":1466415755531,"action":"login","user":"12200000000","password":"12345"}')
print(r.read().decode("utf-8"))
print(cj)
# r=opener.open('https://200.200.169.212/server/index.php/mod_workreport',
#               data=b'{"wrdate":1485878400000,"reportType":2,"opr":"create","content":"55552222","attrs":[]}')
test_data='{"wrdate":1485878400000,"reportType":2,"opr":"create","content":"55552222","attrs":[]}'
url='https://200.200.169.212/server/index.php/mod_workreport'+'?'+test_data
url='https://200.200.169.212/server/index.php/mod_workreport?{"wrdate":1485878400000,"reportType":2,"opr":"create","content":"55552222","attrs":[]}'

print("--------------")
r=urllib.request.urlopen(url)
print(r.read().decode("utf-8"))