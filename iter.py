list = [1, 2, 3, 4]
it = iter(list)   #创建迭代器对象
print(next(it))   #输出迭代器的下一个元素  1

print(next(it))   # 2

print('\n--------------------------------------------')


list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=' ')

print('\n--------------------------------------------')


#使用next函数

import sys
list = [1, 2, 3, 4]
it = iter(list)               # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:     # try except语句块捕获并处理异常
        sys.exit()
