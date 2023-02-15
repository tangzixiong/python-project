
# Python两种输出值的方式: 表达式语句和 print() 函数。
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
# 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。

#   str()： 函数返回一个用户易读的表达形式。
#   repr()： 产生一个解释器易读的表达形式。 


#两种方式输出一个平方与立方的表:

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x**2).rjust(3), end=' ')       #字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格, 类似的方法, 如 ljust() 和 center()
    print(repr(x**3).rjust(4))


print('----------------------------------------------------------------------------------')


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))


# zfill(), 它会在数字的左边填充 0

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))


print('-----------------------------------------------------------------------------------')

# str.format() 的基本使用如下

print('{}网址： "{}!"'.format('牛客教程', 'www.nowcoder.com'))    #括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换



#在括号中的数字用于指向传入对象在 format() 中的位置
print('{0} 和 {1}'.format('Google', 'Nowcoder'))
print('{1} 和 {0}'.format('Google', 'Nowcoder'))


# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
print('{name}网址： {site}'.format(name='牛客教程', site='www.nowcoder.com'))


import math
print('常量 PI 的值近似为 {0:.3f}.'.format(math.pi))

print('常量 PI 的值近似为 %7.3f. ' % math.pi)   # % 操作符也可以实现字符串格式化


print('-------------------------------------------------------------------------------------')

#后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用

table = {'Google': 1, 'Nowcoder': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))



table = {'Google': 1, 'Nowcoder': 2, 'Taobao': 3}
print('Nowcoder: {0[Nowcoder]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

print('Nowcoder: {Nowcoder:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))



print('-------------------------------------------------------------------------------------')


#print 函数默认分隔符为空格，可用 sep 参数指定特定符号作为输出对象的分隔符号

print(1, 'abc', 3, 'ff', sep='$')  #1$abc$3$ff

#print 函数默认以""" 回车换行 """符号作为输出结尾符号，即在输出最后会换行，后面的 print 函数的输出在新的一行开始, 可用 end 参数指定输出结尾符号

print('100', end=',');print('abc')


print('-------------------------------------------------------------------------------------')


#print 函数默认输出到标准输出流，win系统输出到命令行窗口，可用 file 参数指定输出到特定文件
file1 = open('data.txt', 'w')                   #打开文件
print(123, 'abc', 45, 'book', file = file1)     #用file参数指定输出到文件
file1.close()
print(open('data.txt').read())                  #输出从文件中读出的内容




print(~-6)
