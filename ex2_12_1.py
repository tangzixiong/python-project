#分别编写求n！和输出斐波那契数列的函数，并调用两个函数进行测试
def factorial(n):
    r = 1
    while n>1:
        r *= n
        n -= 1
    return r

def fib(n):
    a, b = 0, 1
    while a<n:
        print(a, end=' ')
        a, b = b, a+b

print('%d!=%d' % (5, factorial(5)))
fib(200)