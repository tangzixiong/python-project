#在 Python 中，使用了 yield 的函数被称为生成器（generator）
""" 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点
理解生成器就是一个迭代器。在调用生成器运行的过程中，每次遇到 yield 时函数会
暂停并保存当前所有的运行信息，返回 yield 的值,并在下一次执行 next() 方法时
从当前位置继续运行。调用一个生成器函数，返回的是一个迭代器对象。 """

# 使用 yield 实现斐波那契数列
""" import sys

def fibonacci(n):           # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10)           # f 是一个迭代器， 由生成器返回生成

while True:
    try:
        print (next(f), end=' ')
    except StopIteration:
        sys.exit() """



print('-----------------------------------------------1-------------------------------------------------------')

L = [x * x for x in range(10)]          #列表推导式
G = (x * x for x in range(10))          #生成器推导式
print(L)                                # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(G)                                # <generator object <genexpr> at 0x000002856ED51E00>

print('-----------------------------------------------2-------------------------------------------------------')


def test(n):                            #生成器函数
    for i in range(n):                  #迭代列表
        yield i*i                       #定义生成器中每个元素的值并返回

g = test(10)                            #调用生成器函数， 生成一个生成器对象
print(g)                                #输出 <generator object test at 0x0000026BAEC31E00>
print(next(g))                          #读取第一个元素值


print('-----------------------------------------------3-------------------------------------------------------')

def test(n):                            #生成器函数
    for i in range(n):                  #迭代列表
        yield i*i                       #定义生成器中每个元素的值并返回
    
g = test(5)                             #调用生成器函数，生成一个生成器对象
print(next(g))                          #读取第一个元素值
print(g.__next__())                     #读取第二个元素值
for i in g:                             #读取后面三个元素值
    print(i)


print('-----------------------------------------------4-------------------------------------------------------')

#在迭代生成器过程中，使用send()方法中途改变迭代的次数

def down(n):                #生成器函数
    while n >= 0:           #设置递减循环的条件
        m = yield n         #定义每次迭代生成的值并返回
        if m:               #当条件为True, 则改写递减变量的值
            n = m
        else:               #正常情况下，m为大于0的数字，则递减
            n -= 1

d = down(5)                 #调用生成器函数
for i in d:
    print(i)                #打印元素
    if i == 5:              #当打印完第一个元素后
        d.send(3)           #修改yield表达式的值为3



