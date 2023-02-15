# open() 将会返回一个 file 对象，基本语法格式如下

"""
open(filename, mode)
"""
# filename：包含了你要访问的文件名称的字符串值。
# mode：决定了打开文件的模式：只读，写入，追加等

""" f.read() """

f = open('data2_2.txt','r')
str = f.read()                  # f.read() 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回
print(str)                       # size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回

f.close()           # 关闭打开的文件



print('---------------------------------------------')


""" f.readline() """
# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。 f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行

f = open('data2_2.txt','r')

str1= f.readline()
print(str1)

f.close()           # 关闭打开的文件

print('------------------------------------------------------------------')


""" f.readlines() """
#f.readlines() 将返回该文件中包含的所有行。
#如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割

f = open('data2_2.txt','r')
str2 = f.readlines()
print(str2)

for line in f:
    print(line, end=' ')

f.close()


print('------------------------------------------------------------------')


f = open('data2_2.txt','r')
for line in f:                  #迭代一个文件对象然后读取每行
    print(line, end='')

f.close()






