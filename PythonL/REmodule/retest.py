import re
import urllib
from urllib import request
# e.compile(pattern, flags=0)
# 将正则表达式模式编译成一个正则表达式对象，它可以用于匹配使用它的match ()和search ()方法，如下所述。
#
# 可以通过指定flags值修改表达式的行为。值可以是任何以下变量，使用组合 OR （ |运算符）。
urlstr="http://www.baidu.com"
fp=urllib.request.urlopen(urlstr)

html2str=fp.read().decode("utf8")
fp.close()
#print(html2str)
#提取所有的a标签
rc = re.compile("\<a.*?a\>")
alla = rc.findall(html2str)
#print(alla)
alla1="\n".join(alla)
#print(alla1)
#将所有的标签符号全部替换掉
rsub = re.compile("\<.*?\>")
alla = rsub.sub("",alla1)
print(alla)






