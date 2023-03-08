"""
 open() 方法

Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。 
"""

# open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。

#               open(file, mode='r')

#完整的语法格式为
#                    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 参数说明:
                            # file: 必需，文件路径（相对或者绝对路径）。
                            # mode: 可选，文件打开模式
                            # buffering: 设置缓冲
                            # encoding: 一般使用 utf8
                            # errors: 报错级别
                            # newline: 区分换行符
                            # closefd: 传入的file参数类型
                            # opener: 传递可调用对象


##
""" 
fileObj = open( fileName, mode='r', buffering=-1, encoding=None,
            errors=None, newline=None, closefd=True, opener=None)
"""

##创建新文件
# fileName = "test.txt"                                 #创建的文件名
# try:
#     fp = open(fileName, "a+")                         #创建文件
#     print("%s 文件创建成功" % fileName)                #提示创建成功
# except IOError:
#     print("文件创建失败， %s 文件不存在" % fileName)    #提示创建失败
# finally:
#     fp.close()                                        #关闭文件



## r模式只能打开已存在的文件
# fileName = "test1.txt"              
# try:
#     fp = open(fileName, "r")
# except IOError:
#     print("文件打开失败， %s 文件不存在" % fileName)
# finally:
#     fp.close()


##使用with语句打开文件
"""
with open(文件) as file 对象：
    操作file对象
"""
##在with语句中打开文件，然后逐行读取字符串并打印出来

# with open("test1.txt", "r", encoding="utf-8") as file:
#     for line in file.readline():
#         print(line)

# readline(): 读取文件中的一行，包括\n字符
# readlines(): 读取文件多行数据，然后返回一个列表，可以通过循环访问列表中的元素
# read(): 从文件中一次性读出所有内容，并赋值给一个字符串变量



## 使用f.readline()逐行读取文件中的字符串
f = open("test.txt", "r", encoding='utf-8')
while True:
    #line = f.readline()         #读取每行文本
    line = f.readline(5)        #每次读取5个字节
    if line:                    #如果不是尾行， 则显示读取的文本
        print(line)
    else:                       #如果是尾行，则跳出循环
        break
f.close

print('\n-----------------------------------1-------------------------------------------\n')

##使用readlines()方法读取文件

f = open("test.txt", 'r', encoding='utf-8')
lines = f.readlines()               #读取所有行
for line in lines:                  #从列表中读取每行并显示
    print(line)
f.close


f = open('test.txt', 'r', encoding='utf-8')
all = f.read()                      #读取所有内容
print(all)
f.close

