def fib2(n):    # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)

print(f100)



import fibo      # fibo.py
fibo.fib(1000)


##############输出斐波拉契数列的前n项###########

n = int(input('输出斐波那契数列的前n项:n='))
list=[]
for m in range(0, n):
    if m == 0:
        list.append(0)
    elif m == 1:
        list.append(1)
    else:
        list.append(list[m-1]+list[m-2])
for i in range(len(list)):
    print(list[i], end=' ')
