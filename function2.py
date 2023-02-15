
#不定长参数
#基本语法

""" 
def functionname([formal_args,] *var_args_tuple ):
    "函数_文档字符串"
    function_suite
    return [expression]
"""
# 加了*号的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数

def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print('输出：')
    print(arg1)
    print(vartuple)

# 调用printinfo 函数
printinfo( 70, 60, 50 )


print("------------------------------------------------------------------")

#如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量
def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print ("输出：")
    print (arg1)
    for var in vartuple:
        print (var)
    return

printinfo( 10 )
printinfo( 70, 60, 50 )


print("------------------------------------------------------------------")

""" 
def functionname([formal_args,] **var_args_dict ):
    "函数_文档字符串"
    function_suite
    return [expression]
"""

def printinfo( arg1, **vardict ):   #加了两个星号*的参数会以字典的形式导入
    "打印任何传入的参数"
    print ("输出：")
    print (arg1)
    print (vardict)

printinfo(1, a=2, b=3)

#声明函数时，参数中星号 * 可以单独出现, 如果单独出现星号 * 后的参数必须用关键字传入




#函数嵌套定义

def add(a,b):
    def getsum(x):                          #在函数内部定义的函数，将字符串转换为ASCII求和
        s = 0
        for n in x:
            s+=ord(n)
        return s
    return getsum(a)+getsum(b)             #调用内部定义的函数getsum

print(add('12','34'))


print("------------------------------------------------------------------")


#递归函数

def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)           #求阶乘

print(fac(5))