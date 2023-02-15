#随机数模块
#random.random():用于生成一个-~1.0的随机浮点数(0<=n<1.0)
#random.uniform(a,b):用于生成一个指定范围内的随机浮点数(a<=n<b)
#random.randint(a,b):用于生成一个指定范围内的随机整数(a<=n<=b)
#random.randrange([start=0], stop[, step=1]): 从指定范围内，按指定步长递增的集合中获取一个随机参数
#random.choice(sequence): 从序列sequence对象中获取一个随机元素(可能会重复出现)
#random.shuffle(x[,random]):用于将一个列表中的元素打乱
#random.sample(sequence, k): 从指定序列sequence中随机获取指定长度的片段，参数k表示关键字参数，必须设置，获取元素的个数

import random
print(random.random())
print(random.randint(1,3))
print(random.randrange(1,3))
print(random.choice([1,2,[3,5]]))
print(random.sample([1,'23',[4,5]],3))
print(random.uniform(1,3))


print('------------------------------------1-----------------------------------------')

#使用random模块生成一个4位验证码

import random                                   #导入随机生成器模块
code_list = []
for i in range(4):
    num1 = random.randint(0,9)                  #随机生成一个0~9的数字
    str1 = chr(random.randint(65, 90))          #随机生成一个65~90的数字，然后转成字母
    s = random.choice([num1, str1])             #随机从数字和字母中选择一个元素
    code_list.append(str(s))
code = ''.join(code_list)                       #'sep'.join(sep_object)  sep：分割符，可为“，、；”等。
                                                # sep_object：分割对象，可为字符串、以及储存字符串的元组、列表、字典。
print(code)                                     
