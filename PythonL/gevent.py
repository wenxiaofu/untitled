import gevent
from urllib.request import urlopen
def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))#here is a git test
    #from the pc
gevent.joinall([
        gevent.spawn('https://www.python.org/'),
        gevent.spawn('https://www.yahoo.com/'),
        gevent.spawn('https://github.com/'),
])
