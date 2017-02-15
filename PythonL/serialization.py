# -*- coding: UTF-8 -*-
#python对象序列化成json对象
#python序列化 http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192607210600a668b5112e4a979dd20e4661cc9c97000
import json
d = dict(name='bob',age=20)
f = json.dumps(d)
print(f)
str='{"age":20,"score":60,"name":"bob"}'
print(json.loads(str))

class Student(object):
    pass