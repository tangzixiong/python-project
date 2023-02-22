##递归
#递归技术通过一个函数在执行过程中一次或多次调用，
#是一种通过重复将问题分解为同类的子问题而解决问题的方法


# 阶乘函数的递归实现

def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))



##二分查找 O(logn)
#low = 0,  high = n-1  mid = [(low+high)/2](向下取整)

def binary_search(data, target, low, high):
    
    if low > high:
        return False            #索引范围为空            
    else:
        mid = (low+high)//2
    if target == data[mid]:
        return True
    elif target < data[mid]:        #索引范围为low到mid-1
        return binary_search(data, target, low, mid-1)
    else:                           #索引范围为mid+1到high
        return binary_search(data, target, mid+1, high)
    
    
##报告一个文件系统磁盘使用情况的递归函数

import os

def disk_usage(path):
    total = os.path.getsize(path)           #返回由字符串路径标识的文件或者目录使用的即时磁盘空间大小
    if os.path.isdir(path):                 #如果字符串路径指定的条目是一个目录，则返回True, 否则返回False
        for filename in os.listdir(path):       #os.listdir(path) 返回一个字符串列表，它是字符串路径指定的目录中所有条目的名称
            childpath = os.path.join(path, filename)    #生成路径字符串和文件名字符串
            total += disk_usage(childpath)
            
    print('{0:<7}'.format(total), path)
    return total


##测试元素唯一性的递归函数unique3
def unique3(S, start, stop):
    if stop - start <=1: 
        return True
    elif not unique3(S, start, stop-1):
        return False
    elif not unique3(S, start+1, stop):
        return False
    else:
        return S[start] != S[stop-1]
    

##使用二分递归计算第n个斐波那契数列

def bad_fibonacci(n):
    if n <=1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)
    

##使用线性递归计算第n个斐波那契数

def good_fibonacci(n):
    if n<=1:
        return (n,0)
    else:
        (a,b) = good_fibonacci(n-1)
        return (a+b, a)
    

##使用线性递归计算序列元素的和

def liner_sum(S, n):        #序列S前n个元素的和
    if n == 0:
        return 0
    else:
        return (S, n-1) + S[n-1]
    

##使用线性递归逆置序列的元素
def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop-1]=S[stop-1],S[start]
        reverse(S, start+1, stop-1)
        

##用简单的递归计算幂函数
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
    
##使用重复的平方计算幂函数
def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
            return result
        
##用二路递归计算一个序列的元素之和

def binary_sum(S, start, stop):
    if start >=stop:
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = (start + stop)// 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
        
        
        
##二分查找算法的非递归实现
def binary_search_iterative(data, target):
    low = 0
    high = len(data)-1
    while low <=high:
        mid = (low + high) //2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


##使用迭代逆置一个序列的元素
def reverse_iterative(S):
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        start, stop = start + 1, stop - 1