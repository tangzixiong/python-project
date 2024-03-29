## os 模块

# 原文链接：https://blog.csdn.net/xw1680/article/details/125563034
# Python 标准库之 os 模块详解: http://www.ityouknow.com/python/2019/10/09/python-os-demonstration-026.html

#os模块提供的就是各种 Python 程序与操作系统进行交互的接口。通过使用os模块，一方面可以方便地与操作系统进行交互，
#另一方面页可以极大增强代码的可移植性。

# os 模块是Python内置的与操作系统中的文件系统相关的模块，该模块依赖于操作系统。通常情况下，
# 如不特别指出，该模块提供的方法、属性在Windows 和 UNIX(Linux 和Mac OS X)系统上都是可用的。


##文件路径
# 用于定位一个文件或者目录的字符串被称为路径。在程序开发时，通常涉及到两种路径：一种是相对路径，另一种是绝对路径。

## 相对路径： 在学习相对路径之前，需要先了解什么是当前工作目录，当前工作目录是指当前文件所在的目录。
# 在 Python 中，可以通过 os 模块提供的 getcwd() 方法获取当前工作目录。相对路径是依赖于当前工作目录的。
# 如果在当前工作目录下，有一个名称为 message.txt 的文件，那么在打开这个文件时，就可以直接写文件名，这时采用的就是相对路径

import os

print(os.getcwd())      #打印当前目录


## 绝对路径：绝对路径是指文件的实际完整路径，它不依赖于当前工作目录，从盘符出发。 
# 在Python中，可以通过os.path模块提供的abspath()方法获取一个文件的绝对路径。

import os
#在指定文件路径时，也可以在表示路径的字符串前面加上字母 r(R)，那么该字符串将原样输出，这时路径中的分隔符就不需要再转义了
print(os.path.abspath(r"demo\message.txt"))     # 打印绝对路径


# 如果不确定该模块都提供了哪些属性和方法，可以使用 Python 的内置函数 dir() 获取全部的方法列表，代码如下：

import os       # 导入文件与操作系统相关模块

print(dir(os))