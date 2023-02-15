#Python 定义函数使用 def 关键字，一般格式如下：

""" def 函数名 （参数列表）：
        函数体 
"""

def hello():
    print('hello world')   #return "hello world"

hello()                    #print(hello())


print('----------------------------')


#计算面积函数
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Nowcoder")
w = 4
h = 5
print("width =", w, "height =", h, "area =", area(w, h))



print('---------------------------------------------------------------------------------')

# python 传不可变对象实例

def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print("b=", b)      # 结果是 2


print('----------------------------------------------------------------------------------')

# python 传可变对象实例

def changeme( mylist ):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值：", mylist)
    return 

mylist = [10, 20, 30]
changeme( mylist )
print("函数外取值： ", mylist)      #传入函数的和在末尾添加新内容的对象用的是同一个引用


print('-----------------------------------------------------------------------------------')


def f(a):
    a[0]='abc'                      #修改列表第一个值

x=[1,2]
f(x)                                #调用函数，传递列表对象的引用
print(x)                            #变量x引用的列表对象在函数中被修改  输出 ['abc', 2]

#如要避免列表在函数中被修改，可使用列表的拷贝作为实参

def f(a):
    a[0]='abc'

x=[1,2]
f(x[:])                            #传递列表的拷贝
print(x)                           #[1, 2]


#函数内对列表进行拷贝，实参仍使用变量
def f(a):
    a=a[:]                      #拷贝列表
    a[0]='abc'

x=[1,2]
f(x)                            #调用函数
print(x)



def add(a,b=-100):  #默认值参数，调用函数时如未提供实参，则形参取默认值
    return a+b

print(add(1,2))
print(add(1))

print('-----------------------------------------------------------------------------------')


def add(a,*b):
    s=a
    for x in b:             #用循环迭代元组b中的对象
        s+=x                #累加
    return s

print(add(1,2))
print(add(1,2,3,4,5))



#必须通过赋值传递的参数

def add(a,*b,c):
    s=a+c
    for x in b:
        s+=x
    return s

print(add(1,2,3,c=4))

print(add(1,c=3))



