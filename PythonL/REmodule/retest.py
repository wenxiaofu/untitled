import re
import urllib
from urllib import request
# e.compile(pattern, flags=0)
# 将正则表达式模式编译成一个正则表达式对象，它可以用于匹配使用它的match ()和search ()方法，如下所述。
#
# 可以通过指定flags值修改表达式的行为。值可以是任何以下变量，使用组合 OR （ |运算符）。
urlstr="http://200.200.107.38/m/James/order/pp15_1_-_%E5%BA%94%E7%94%A8_-_%E9%94%80%E5%94%AE%E8%AE%A2%E5%8D%95_-_%E8%AE%A2%E5%8D%95%E5%88%97%E8%A1%A8.html"

fp=urllib.request.urlopen(urlstr)

html2str=fp.read().decode("utf8")
fp.close()
#print(html2str)
#提取所有以<span开头</span>结尾的数据
#提取方式(\<span\>\&\#149\;.*?span\>)|
a="(\<span\>.*?span\>)|(\<span\>\&\#149\;.*?span\>)"
a="(\<span\>.*?span\>)"
rc = re.compile(a)
#alla = rc.findall(html2str)
alla=re.findall(a,html2str)
#print(alla)
alla1="\n".join(alla)
#print(alla1)
#将所有匹配到的标签符号全部替换掉
rsub = re.compile("\<.*?\>")
alla = rsub.sub("",alla1)
print(alla)






