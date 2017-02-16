#list
#生成list
li=list(range(1,10))
print(li)

for i in range(1,10):
    print(i)

li=[ x*x for x in range(1,10) ]
print(li)

#可以增加多个条件
print([x * x for x in range(1, 11) if (x % 2 == 0 and x!=2)])
