#异常处理

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number.  Try again  ")



""" 
try语句按照如下方式工作;

            首先,执行try子句(在关键字try和关键字except之间的语句)
            如果没有异常发生,忽略except子句,try子句执行后结束。
            如果在执行try子句的过程中发生了异常,那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符,那么对应的except子句将被执行。最后执行 try 语句之后的代码。
            如果一个异常没有与任何的except匹配,那么这个异常将会传递给上层的try中。

一个 try 语句可能包含多个except子句,分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的try子句中的异常进行处理,而不是其他的 try 的处理程序中的异常。
"""

##一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
        
""" except (RuntimeError, TypeError, NameError):
            pass
"""

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())                      #str.strip([chars])
                                            #返回原字符串的副本，移除其中的前导和末尾字符。 chars 参数为指定要移除字符的字符串。 如果省略或为 None，则 chars 参数默认移除空白符。
except OSError as err:
    print("OS error: {0}" .format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexcepted error:", sys.exc_info()[0])
    raise


#try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')



def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
