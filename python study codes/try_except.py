##try和except语句组合可以捕获并处理异常
""" try:
        语句块                      #可能产生异常的代码
    except 异常名称 [ as 别名]:     #要处理的异常类型
        语句块                      #当异常发生时执行
"""

##设计捕获所有的异常
try:
    5/0
except:                         #捕获所有的异常
    print('不能除以 0 ')         #提示错误信息
print('程序继续执行')            #继续执行代码


print('----------------------------------1----------------------------------------')

try:
    f = open("a.txt", "r")                      #打开并不存在的文件
except IOError as e:                            #捕获IOError类型异常
    print("错误编号: %s, 错误信息: %s" % (e.errno, e.strerror))         #显示错误信息



print('----------------------------------2----------------------------------------')

#使用Exception类型可以捕获所有常规异常
try:
    f = open("a.txt", "r")                  #打开并不存在的文件
except Exception as e:                      #捕获IOError类型异常
    print("错误编号: %s, 错误信息：%s" %(e.errno, e.strerror))      #显示错误信息
                                                                  #输出：错误编号: 2, 错误信息：No such file or directory

print('----------------------------------3----------------------------------------')

#设计一个多层嵌套的异常处理结构，演示异常传递的过程
try:
    try:
        try:
            f = open("a.txt","r")           #打开并不存在的文件
        except NameError as e:              #捕获未声明的变量的异常
            print("NameError")              #显示错误信息
    except IndexError as e:                 #捕获索引超出列表范围的异常
        print("IndexError")                 #显示错误信息
except IOError as e:                        #捕获输入/输出的异常
    print("IOError")                        #显示错误信息



print('\n----------------------------------4----------------------------------------\n')

##捕获多个异常

#一个except语句包含多个异常，多个异常以元组形式设置
""" 
try:
    语句块                                  #可能产生异常的代码
except (异常名1, 异常名2, ...) [as 别名]:
    语句块                                  #对异常进行处理的代码
"""

#使用多个except语句处理异常，多个异常之间存在优先级
""" 
try:
    语句块                      #可能产生异常的代码
except 异常名1 [as 别名1]:
    语句块                      #对异常进行处理的代码
except 异常名1 [as 别名1]:
    语句块
except 异常名1 [as 别名1]:
    语句块
"""


import requests                                         #导入request模块
from requests import ReadTimeout                        #导入ReadTimeout异常类
url = 'https://www.baidu.com'
try:
    response = requests.get(url, timeout=1)             #发出请求
    if response.status_code == 200:                     #如果请求成功，则打印请求的网页源代码
        print(response.text)
    else:                                               #如果请求失败，则打印响应的状态码
        print('Get page Failed', response.status_code)
except (ConnectionError, ReadTimeout):                  #如果发生异常，则捕获并进行提示
    print('Crawling Failed', url)


print('\n----------------------------------5----------------------------------------\n')

##使用多个except语句捕获异常，并打印异常类型的字符串表示
str1 = 'hello world'
try:
    int(str1)                   #传入非法的值
except IndexError as e:         #捕获IndexError异常
    print(e.__str__)
except KeyError as e:           #捕获KeyError异常
    print(e.__str__)
except ValueError as e:         #捕获ValueError异常
    print(e.__str__)            #输出 <method-wrapper '__str__' of ValueError object at 0x000001AE4553FF10>


print('\n----------------------------------6----------------------------------------\n')

##在 try...except 语句后添加一个可选的else语句，当try语句没有异常时，需要执行的代码块
""" 
try:
    代码块             #可能产生异常的代码
except:
    代码块             #当异常发生时执行
else:
    代码块             #当异常未发生时执行
finally:
    语句块             #不管异常是否发生, 最后都要执行
"""

try:
    f = open("test.txt","r")        #打开文件
except:
    print("出错了")
else:
    print(f.read())                 #读取文件内容



try:
    r = 10/0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')


print('\n----------------------------------7----------------------------------------\n')

##raise语句可以主动抛出异常
"""
 raise [Exception [, args [, traceback]]] 
其中Exception表示异常的类型， args是一个可选的异常参数，默认为None， traceback 表示跟踪异常的回溯对象
"""

def test(num):
    try:
        if type(num) != int:                         #如果为非数字的值，则抛出TypeError错误
            raise TypeError('参数不是数字')
        if num <=0:                                  #如果为非正整数，则抛出ValueError错误
            raise ValueError('参数为大于0的整数')
        print(num)
    except Exception as e:
        print(e)
test("1")
test(0)
test(2)


print('\n----------------------------------8----------------------------------------\n')

##自定义异常类型

class MyError(Exception):               #自定义异常类型
    def __init__(self,msg):             #重写类型初始化函数
        self.msg=msg
    def __str__(self):                  #重写类型标识函数
        return self.msg
    
try:
    raise MyError("自定义错误信息")      #主动抛出自定义错误
except MyError as e:
    print(e)                            #打印：自定义错误信息

