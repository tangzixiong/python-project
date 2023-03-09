##python 高阶函数

## 高阶函数概念：在函数式编程中，我们可以将函数当作变量一样自由使用。
# 一个函数接收另一个函数作为参数，这种函数称之为高阶函数。

def high_func(f, arr):
    return [f(x) for x in arr]

# 其中第一个参数 f 是一个函数，第二个参数 arr 是一个数组，
# 返回的值是数组中的所有的值在经过 f 函数计算后得到的一个列表


from math import factorial

def high_func(f, arr):
    return [f(x) for x in arr]

def square(n):
    return n ** 2

#使用python自带数学函数
print(high_func(factorial, list(range(10))))        #factorial 阶乘函数

print(high_func(square, list(range(10))))



##常用高阶函数

""" map """
#根据提供的函数对指定序列做映射, 并返回映射后的序列，定义：
""" map(func, *iterables) --> map object """

# function : 序列中的每个元素需要执行的操作, 可以是匿名函数
# *iterables : 一个或多个序列

from math import factorial

def square(n):
    return n ** 2

facMap = map(factorial, list(range(10)))
print(list(facMap))

squareMap = map(square, list(range(10)))
print(list(squareMap))



#使用匿名函数，也可以传入多个序列

#使用匿名函数
lamMap = map(lambda x: x * 2, list(range(10)))
print(list(lamMap))


#传入多个序列
mutiMap = map(lambda x, y: x+y, list(range(10)), list(range(11,15)))
print(list(mutiMap))        #[11, 13, 15, 17]



#####################################################################

""" reduce """
#reduce 函数需要传入一个有两个参数的函数，然后用这个函数从左至右顺序遍历序列并生成结果，定义如下：

""" reduce(function, sequence[, initial]) -> value """

    # function # 函数, 序列中的每个元素需要执行的操作, 可以是匿名函数
    # sequence # 需要执行操作的序列
    # initial # 可选，初始参数


from functools import reduce

result = reduce(lambda x, y: x+y, [1,2, 3, 4, 5])
 
print(result)   #15 序列 [1, 2, 3, 4, 5] 通过匿名函数进行了累加。

#设定初始参数
s = reduce(lambda x, y: x+y, ['1', '2', '3', '4', '5'], "数字=")
print(s)



######################################################################

""" filter """
# filter() 函数用来过滤序列中不符合条件的值，返回一个迭代器，该迭代器生成那些函数(项)为
# true 的 iterable 项。如果函数为 None，则返回为 true 的项。定义如下：

""" filter(function or None, iterable) --> filter object """

    # function or None # 过滤操作执行的函数
    # iterable # 需要过滤的序列
    
    
def boy(n):
    if n % 2 == 0:
        return True
    return False

#自定义函数
filterList = filter(boy, list(range(20)))

print(list(filterList))

filterList2 = filter(lambda n: n % 2 == 0, list(range(20)))

print(list(filterList2))




#########################################################################

""" sorted """
# sorted 函数默认将序列升序排列后返回一个新的 list，还可以自定义键函数来进行排序，也可以
# 设置reverse 参数确定是升序还是降序，如果 reverse = True 则为降序。

    # iterable # 序列
    # key # 可以用来计算的排序函数。
    # reverse # 排序规则，reverse = True 降序，reverse = False 升序(默认）。
    
list01 = [5, -1, 3, 6, -7, 8, -11, 2]
list02 = ['apple', 'pig', 'monkey', 'money']

print(sorted(list01))

print(sorted(list01, key=abs))

print(sorted(list02))

print(sorted(list02, reverse=True))

print(sorted(list02, key=lambda x: len(x), reverse = True))