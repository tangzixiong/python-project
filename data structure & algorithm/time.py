
### timeit模块
#timeit模块可以用来测试一小段Python代码的执行速度

## class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)
    # Timer是测量小段代码执行速度的类。
    # stmt参数是要测试的代码语句（statment）；
    # setup参数是运行代码时需要的设置；
    # timer参数是一个定时器函数，与平台有关。

## timeit.Timer.timeit(number=1000000)
    # Timer类中测试语句执行速度的对象方法。number参数是测试代码时的测试次数，默认为1000000次。方法返回执
    # 行代码的平均耗时，一个float类型的秒数。
  
  
    
    
##list的操作测试

def test1():
    l = []
    for i in range(1000):
        l = l + [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))
    
from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat", t1.timeit(number=1000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append", t2.timeit(number=1000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension", t3.timeit(number=1000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range", t4.timeit(number=1000), "seconds")


# concat 0.6262535129999378 seconds
# append 0.02917933000026096 seconds
# comprehension 0.01575837699965632 seconds
# list range 0.006767560999833222 seconds

print('-----------------------1-------------------------------')

## pop操作测试
# from timeit import Timer

# x = range(2000000)
# pop_zero = Timer("x.pop(0)", "from __main__ import x")
# print("pop_zero", pop_zero.timeit(number=1000), "seconds")
# x = range(2000000)
# pop_end = Timer("x.pop()", "from __main__ import x")
# print("pop_end", pop_end.timeit(number=1000), "seconds")

import timeit

def t():
    list_1 = list(range(100))
    for i in range(50):
        list_1.pop()        #pop最后一个元素
        
def t0():
    list_2 = list(range(100))
    for i in range(50):
        list_2.pop(0)       #pop 第一个元素
        
def t10():
    list_2 = list(range(100))
    for i in range(50):
        list_2.pop(10)      #pop第10个元素
        
time = timeit.Timer("t()", "from __main__ import t")
time0 = timeit.Timer("t0()", "from __main__ import t0")
time10 = timeit.Timer("t10()", "from __main__ import t10")
print("pop():%f" % time.timeit())
print("pop(0):%f" % time0.timeit())
print("pop(10):%f" % time10.timeit())               ## 速度：pop()>pop(10)>pop(0)