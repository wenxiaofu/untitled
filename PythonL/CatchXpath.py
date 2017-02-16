from urllib import request
import urllib
import re
from lxml import etree
#first step get the page
f = urllib.request.urlopen('http://200.200.107.38/m/James/order/pp15_1_-_%E5%BA%94%E7%94%A8_-_%E9%94%80%E5%94%AE%E8%AE%A2%E5%8D%95_-_%E8%AE%A2%E5%8D%95%E5%88%97%E8%A1%A8.html')

#       从字符串常量解析HTML文档。 返回根
#        节点（或解析器目标返回的结果）。 这个功能
#        可以用于在Python代码中嵌入“HTML文字”。
element=str(f.read().decode('utf-8'))

#print(element)

li=re.findall(r"\<span\>(.+?)\<\/span\>", element, re.S)
print(li)