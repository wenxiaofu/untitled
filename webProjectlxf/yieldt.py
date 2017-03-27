def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            print('not any product %s' %n)
            r = 'not ok'
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    i = 0
    num = 5
    while i < num:
        r = c.send(i)

        print('[PRODUCER] Producing %s...' % i)
        r = c.send(i)
        i +=1
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)