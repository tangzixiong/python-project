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