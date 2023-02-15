# break 语句用于跳出当前循环， 即提前结束循环（包括跳过else)
#continue语句则用于跳过循环体剩余语句，回到循环开头开始下一次迭代



""" 用for循环找出100-999范围内的前10个回文数 """

a = []
n = 0
for x in range(100, 999):
    s = str(x)
    if s[0]!=s[-1]:continue         #如果不是回文数，跳到循环开头，x取下一个值开始循环
    a.append(x)                       
    n+=1
    if n==10:break                  #找出10个回文数字时，跳出for循环
else:
    print('loop over')
print(a)                            #前面的break跳出时，跳转到此处执行


print('-------------------------------------------------------------------------')


""" 找出100以内的素数 """           

print(2, 3, end=' ')
for x in range(4, 100):
    for n in range(2, x):           #嵌套使用for循环
        if x % n == 0:
            break
    else:
        print(x, end=' ')
else:
    print('over')


print('-------------------------------------------------------------------------')


#while循环在测试条件为真时执行循环体，也称“当型循环”
s = 0
n = 1
while n <= 100:
    s=s+n
    n=n+1
print('1+2+3+...+100 =',s) 



x = 2
while x < 100:
    n = 2
    while n < x-1:
        if x % n == 0:break
        n+=1
    else:
        print(x, end=' ')
    x+=1
else:
    print('over')


print('-------------------------------------------------------------------------')

#嵌套使用while循环 输出99乘法表

a = 1
while a < 10:
    b=1
    while b <= a:
        print('%d*%d=%2d' % (a, b, a*b), end=' ')
        b+=1
    print()
    a+=1






