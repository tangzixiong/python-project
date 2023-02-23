##类的特殊成员

## __doc__   表示类的描述信息，定义在类的第一行注释，通过类对象直接访问

class Test:
    """ Test 空类 
    暂时没有任何代码
    """
    pass
print(Test.__doc__)

print('-------------------------------------------1-----------------------------------------------------------')

##__module__ 和 __class__
#__module__ 表示当前操作的对象属于哪个模块， __class__表示当前操作的对象属于哪个类

class Student:
    def __init__(self, name, age):
        self.n = name
        self.a = age
    
student=Student('bob',22)
print(student.__module__)           #输出 __main__  表示当前文档
print(student.__class__)            #输出 <class '__main__.Student'>


print('-------------------------------------------2-----------------------------------------------------------')


##__new__()
##__new__()表示类的实例化方法， 在创建实例时被自动执行， 且先于__init__()函数之前执行，__new__()方法会返回一个实例， 而 __init__()函数会返回 None

class F:
    def __init__(self, name):                           #初始化函数
        self.name = name
        print("Foo __init__")
    def __new__(cls, *args, **kwargs):                  #实例化创建函数
         print("Foo __new__", cls, *args, **kwargs)

f = F("test")                                           #实例化类

print('--------------------------------------------3----------------------------------------------------------')


class F:
    def __init__(self, name):
        self.name = name
        print("Foo __init__")
    def __new__(cls, *args, **kwargs):          #cls表示传入的类F
        cls.name = "test"                       #创建对象是定义静态变量
        return object.__new__(cls)              #继承父类的__new__()方法
    
f = F('ok')                                     #实例化类
print(F.name)                                   #输出为test
print(f.name)                                   #输出为ok


#创建一个永远保留两位小数的float类型
class RoundFloat(float):
    def __new__(cls, value):
        return super().__new__(cls, round(value, 2))

print(RoundFloat(3.14159))

print('--------------------------------------------4----------------------------------------------------------')



##__init__() 表示类的初始化函数, 在实例化类的过程中被自动调用

## 数据库访问类,可在初始化函数中完成数据库的登录和验证工作

import MySQLdb
class DB:
    def _init_(self, name, password):       #初始化函数, 完成数据库连接操作
        self.__name = name
        self.__password = password
        self.__db = MySQLdb.connect("localhost", name, password, "DatabaseName", charset='utf8')
    def getData(self, sql):                 #查询数据
        pass
    def updateData(self, id):               #更新记录
        pass
    def delData(self, id):                  #删除记录
        pass


print('---------------------------------------------5---------------------------------------------------------')

##__call__() 当使用小括号调用类对象时,将触发执行__new__()方法,即创建类的实例, 同时还会出发__initial__的执行; 
#当使用小括号调用实例对象时, 将触发执行__call__()

##设计一个加法分类器, 允许当类实例化时初始传入多个数字, 调用对象, 继续传入并返回他们的和

class Add:
    """ Add加法分类器，
    可在实例化时传入多个数字，调用对象时也可以继续传入多个数字，然后返回他们的和 """
    def __init__(self, *args):
        self.__sum = 0          #配置存储器变量
        for i in args:          #迭代参数列表
            if (isinstance(i, (int, float))):   #检测参数值是否为数字
                self.__sum +=i                  #叠加数字
    def __call__(self, *args):                  #当调用对象时， 可以传入多个值，并返回和
        for i in args:                          #迭代参数列表
            if (isinstance(i, (int, float))):
                self.__sum +=i
        return self.__sum
    def __del__(self):                          #析构函数
        self.__sum = 0                          #恢复存储器为0

add = Add()
print(add(3,4,5))
add = Add(1,2,3)
print(add(3,4,5))



print('---------------------------------------------6---------------------------------------------------------')

##__dict__ 获取类对象或实例对象包含的所有成员
# 定义一个Test类，包含一个静态字段ver和两个函数__init__()和func(), 同时定义两个普通字段name和password 

class Test:
    ver = 'test'
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def func(self, *args, **kwargs):
        print('func')

print(Test.__dict__)                #获取类的成员， 即静态字段、方法
#{'__module__': '__main__', 'ver': 'test', '__init__': <function Test.__init__ at 0x0000023C16266560>, 
# 'func': <function Test.func at 0x0000023C162664D0>, '__dict__': <attribute '__dict__' of 'Test' objects>,
#  '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}

obj1 = Test('other', 10000)         #实例化
print(obj1.__dict__)                #获取对象obj1的成员  {'name': 'other', 'password': 10000}
obj2 = Test('this', 3888)           #实例化
print(obj2.__dict__)                #获取对象obj2的成员  {'name': 'this', 'password': 3888} 

print('--------------------------------------------7----------------------------------------------------------')


##__str__() 返回实例对象的字符串表示

class Test:
    def __str__(self):
        return "Test类的实例"
    
test = Test()
print(test)


print('------------------------------------------8------------------------------------------------------------')


##__getitem__()、__setitem__()和__delitem__()
#主要用于序列的索引、切片、以及字典的映射操作，分别表示获取、设置、和删除数据


#使用 __getitem__()、__setitem__()和__delitem__()方法模拟设计一个字典操作类
class Dict:                                     #模拟字典类
    def __init__(self, **args):                 #初始化字典对象
        self.__item = args
    def __getitem__(self, key):                 #访问字典元素
        return self.__item.get(key)
    def __setitem__(self, key, value):          #添加字典元素
        if key in self.__item: del self.__item[key]         #先检测是否存在， 如果存在先删除
        return self.__item.setdefault(key, value)           #设置新键
    def __delitem__(self, key):                             #删除字典元素
        return self.__item.pop(key, None)
    
dict = Dict()                   #构建一个空字典对象
print( dict['a'] )                   #自动触发执行 __getitem__, 输出为None
dict['b'] = 'test'              #自动触发执行 __setitem__
print( dict['b'] )                   #自动触发执行 __getitem__, 输出为test
del dict['b']                   #自动触发执行 __delitem__
print( dict['b'] )                   #自动触发执行 __getitem__, 输出为None
dict = Dict(a=1,b=2,c=3)        #构建一个包含3个键值对的字典对象
print( dict['a'] )                   #自动触发执行 __getitem__, 输出为1
dict['b']='test'                #自动触发执行 __setitem__
print( dict['b'] )                   #自动触发执行 __getitem__, 输出为test
del dict['b']                   #自动触发执行 __delitem__
print( dict['b'] )                   #自动触发执行 __getitem__, 输出为None

print('------------------------------------------9------------------------------------------------------------')

#使用 __getitem__()、__setitem__()和__delitem__()方法模拟__getslice__()、__setslice__()和__delslice__()方法的列表切片功能

class List:
    def __init__(self, *args):                                  #初始化列表对象
        self.__item = list(args)
    def __getitem__(self, index):                               #读取切片， 参数index表示slice(切片)实例
        if isinstance(index, slice):    #isinstance判断一个对象的变量类型 
            return self.__item[index.start:index.stop:index.step]
        return self.__item
    def __setitem__(self, index, value):                        #写入切片，参数index表示slice(切片)实例
        if isinstance(index, slice):
            self.__item[index.start:index.stop:index.step] = value
        return self.__item
    def __delitem__(self, index):                               #删除切片， 参数index表示slice(切片)实例
        if isinstance(index, slice):
            del self.__item[index.start:index.stop:index.step]
        return self.__item

L = List(1,2,3,4,5,6)                       #实例化列表对象
print(L[2:4])                               #读取切片 输出[3,4]
L[-1:5] = [1,2, 3]                          #写入切片
print( L[::] )                              #输出为 [1, 2, 3, 4, 5, 1, 2, 3, 6]
del L[3:5]                                  #删除切片
print( L[::] )                              #输出为 [1, 2, 3, 1, 2, 3, 6]



print('------------------------------------------10------------------------------------------------------------')


##__iter__()方法用于返回迭代器

class Test:
    def __init__(self, sq=[]):          #初始化参数为一个空列表对象
        self.sq = sq                    #存储列表对象到本地字段中
    def __iter__(self):                 #设计迭代器
        return iter(self.sq)            #返回用iter()函数包装的迭代器，迭代参数列表
    
obj = Test([1,2,3,4,5])                 #实例化Test类，并传入列表参数
for i in obj:                           ##实例化Test类后，可使用for语句迭代实例对象
    print(i)

print('------------------------------------------11------------------------------------------------------------')

##__del__()析构函数，当实例对象在内存中被释放时，会被自动触发执行

class DB:
    def __init__(self, name, password):         #初始化函数
        self.__name = name
        self.__password = password
        self.__db = MySQLdb.connect("localhost", name, password, "DatabaseName", charset = 'utf8')
    def __del__(self):                          #析构函数
        self.__db.close()                       #关闭数据库连接


print('------------------------------------------12------------------------------------------------------------')

##__getattr__(), __setattr__()和__delattr__() 三个方法主要用于对象的属性操作，
#分别表示获取、 设置、 和删除属性值

class Student:                                  #定义student类
    def __init__(self, id, name, gender):       #初始化函数
        self.id = id                            #定义属性
        self.name = name
        self.gender = gender
    def __getattr__(self, item):                #定义获取容器中指定属性的行为
        print('no attribute', item)
        return False
    def __setattr__(self, key, value):          #定义设置容器中指定属性的行为
        self.__dict__[key] = value
    def __delattr__(self, item):                #定义删除容器中指定属性的行为
        print('beginning remove', item)
        self.__dict__.pop(item)                 #删除指定属性
        print('remove finished')

student = Student('2019123456','bob', 'male') 
print(student.age)                              #获取不存在的age属性值
student.age = 18                                #设置属性
print(student.age)
print(student.__dict__)                         #打印类中所有对象的成员
del student.age                                 #删除age属性
print(student.__dict__)

print('------------------------------------------13------------------------------------------------------------')

## __lt__、__le__、__gt__、 __ge__、 __eq__ 和 __ne__
#__lt__(self, other): 小于 <
#__le__(self, other): 小于等于 <=
#__gt__(self, other): 大于
#__ge__(self, other): 大于等于
#__eq__(self, other): 等于 ==
#__ne__(self, other): 不等于！=


class Sentence(str):
    def __init__(self, a):
        if isinstance(a, str):
            self.len = len(a)
        else:
            print('TypeError')
    def __gt__(self, other):
        if self.len > other.len:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.len >= other.len:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.len < other.len:
            return True
        else:
            return False
    def __le__(self, other):
        if self.len <= other.len:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.len == other.len:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.len != other.len:
            return True
        else:
            return False
        
a = Sentence('Hello world')
b = Sentence('Nice to meet you')
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)


print('------------------------------------------14------------------------------------------------------------')

##__base__ 和 __bases__ 属性表示类的基类
#如果是单继承使用__base__可以获取父类，  多继承使用__bases__可以获取所有父类， 并以元组类型返回

class Parent:
    name = '父类'
class Son(Parent):
    name = '子类'

print(Son.__base__)             #  <class '__main__.Parent'>
print(Son.__bases__)         # (<class '__main__.Parent'>,)


print('------------------------------------------15------------------------------------------------------------')

class Parent1:
    name = '父类1'
class Parent2:
    name = '父类2'
class Son(Parent1, Parent2):
    name = '子类'

print(Son.__base__)             #输出为<class '__main__.Parent1'>
print(Son.__bases__)            #输出为(<class '__main__.Parent1'>, <class '__main__.Parent2'>)

print('------------------------------------------15------------------------------------------------------------')


##__add__、 __sub__、 __mul__、 __truediv__ 和 __mod__

#__add__(self, other)：+
#__sub__(self, other)：-
#__mul__(self, other)：*
#__truediv__(self, other)： 真除法 /
#__floordiv__(self, other)：整数除法 //
#__mod__(self, other)：取余运算 %

class Vector:                   #定义向量类
    def __init__(self, x, y):   #初始化类
        self.x = x
        self.y = y
    def __str__(self):          #输出格式
        return 'Vector(%d, %d)'%(self.x, self.y)
    def __add__(self, other):                                      #重写加法方法，参数other是Vector类型
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):                                      #重写减法方法，参数other是Vector类型
        return Vector(self.x - other.x, self.y - other.y)

vector1 = Vector(3, 5)
vector2 = Vector(4, -6)
print(vector1, '+', vector2, '=', vector1 + vector2 )
print(vector1, '-', vector2, '=', vector1 - vector2 )
