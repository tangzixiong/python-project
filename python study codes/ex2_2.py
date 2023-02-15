#统计data2_2.txt中五行字符串中字符a、c、g、t出现的频数

import numpy as np
a = []
with open('data2_2.txt') as f:
    for (i, s) in enumerate(f):
        a.append([s.count('a'), s.count('c'),
            s.count('g'), s.count('t')])
b=np.array(a); print(b)


""" 
enumerate(iterable, start=0)
返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。
 enumerate() 返回的迭代器的 __next__() 方法返回一个元组，里面包含一个计数值
 （从 start 开始，默认为 0）和通过迭代 iterable 获得的值。 
"""