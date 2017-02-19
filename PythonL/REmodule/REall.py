import re
'''
相对详细点的中文blog
http://www.cnblogs.com/yangxiaolan/p/5639538.html
http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
1 匹配正则（常用）
1）^a以a开头
2) +匹配一次或者无限次
3）* 匹配0次或者无限次
4）（...）被括号括起来的将作为一个分组，分组后面也可以接数量词汇
5）？匹配0次或者一次
6）[...]  字符集 例：[a-z];

2 主要方法
re.compile():定义正则匹配方式
re.search()：匹配字符串的任意位置，只返回第一次匹配到的结果
re.match()：只是匹配字符串的开始位置
re.split()：按照参数出现的次数将字符分成若干个数组，好像字符自带这种方法
re.sub():将匹配的字符替换成自己想要的字符

3 匹配模式
re.S：有这个标识可以匹配换行符号，没有则不能匹配换行符号
re.M:多行匹配
re.I:不区分大小写


'''
#下面例子，从一段代码中提取我们想要的web_session的值，在编写网络爬虫的时候经常需要提取服务端返回的session
#如果服务端范围的是标准的json格式，我们也可以是直接使用python来解析，这里是正则的方式

statment='''
here is a cookie
{"web_token":"usename",
 "web_session":"ddauehhteaeee",qitadeneirong,
 session=notallofyou
}
'''


#定义匹配方式:正则解析：已web_session开始，已双引号结束  .*是贪婪模式会匹配web_session后面所有字符到换行符号为止
#后面加上?加双引号表示已双引号结尾
cl = re.compile(r'"web_session":".*?"',re.M);

#mt = cl.match(statment)
#print(mt)
#se = cl.search(statment)
#print(se)
fd = cl.findall(statment)
print(fd)
#替换掉双引号，冒号，和web_sesion,这样就提取出来了seb_ssession的值
cl1=re.compile(r'"web_session"|"|:',re.M)
d=cl1.sub("",fd[0])
print(d)

# print(cl1.sub(fd[0]))

#测试re.compile
'''
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")
string="dsdf 12.23,meiyou : 17.12"
print(a.findall(string))
print(b.findall(string))
'''


