def factorial(n): #定义阶乘函数
    r = 1
    while n>1:
        r *= n
        n -= 1
    return r

def fib(n):  #定义输出斐波那契数列
    a, b = 0, 1
    while a<n:
        print(a, end=' ')
        a, b = b, a+b