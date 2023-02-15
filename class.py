# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。

"""                     
    class ClassName:
         <statement-1>
         .
         .
         .
         <statement-N> 
"""

# 类对象支持两种操作：属性引用和实例化。

# 属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。

# 类对象创建后，类命名空间中所有的命名都是有效属性名。



class MyClass:
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass()       # 实例化类

# 访问类的属性和方法
print('MyClass 类的属性 i 为：', x.i)
print(type(x.i))
print('MyClass 类的方法 f 输出为：', x.f())
print(type(x.f()))


print('---------------------------------------------------------------------------------------------')


#类有一个名为 init() 的特殊方法（构造方法），该方法在类实例化时会自动调用
""" 
def __init__self():
    self.data = []
"""

class Complex:
    def __init__(self, realpart, imagpart):        #self代表类的实例，而非类
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)

print('---------------------------------------------------------------------------------------------')


#类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self

class Test:
    def prt(self):
        print(self)
        print(self.__class__)  #self.__class__可访问实例对象的类

t = Test()
print(t.prt())             #self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类

print('----------------------------------------------------------------------------------------------')


#在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数

class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说： 我 %d 岁。" %(self.name, self.age))
# 实例化类
p = people('nowcoder', 10,30)
p.speak()



print('------------------------------------------------------------------------------------------------')



#Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:

""" 
                class DerivedClassName(BaseClassName1):
                    <statement-1>
                    .
                    .
                    .
                    <statement-N>
"""

#注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法
                                

#BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:


""" class DerivedClassName(modname.BaseClassName): """


#单继承示例
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        #调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了， 我在读 %d 年级"%(self.name, self.age, self.grade))

s = student('ken', 10, 60, 3)
s.speak()



print('--------------------------------------------------------------------------------------------------------')


#Python同样有限的支持多继承形式。多继承的类定义形如下例:

""" 
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N> 
"""

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性，在类外部无法直接进行访问
    __weight =0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我 %d岁。" %(self.name, self.age))

#单继承
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        #调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说： 我 %d 岁了， 我在读 %d 年级" % (self.name, self.age, self.grade))

#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s, 我是一个演说家，我演讲的主题是 %s" %(self.name, self.topic))

#多重继承
class sample(speaker, student):
    a =''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample("Tim", 25, 80, 4, "python")
test.speak()            #我叫 Tim, 我是一个演说家，我演讲的主题是 python



print('------------------------------------------------------------------------------------------------------')

#方法重写, 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法

class Parent:               # 定义父类
    def myMethod(self):
        print('调用父类方法')

class Child(Parent):        #定义子类
    def myMethod(self):
        print ('调用子类方法')

c = Child()                 #子类实例
c.myMethod()                #子类调用重写方法
super(Child,c).myMethod()   #用子类对象调用父类已被覆盖的方法           #super() 函数是用于调用父类(超类)的一个方法。


print('------------------------------------------------------------------------------------------------------')


#类的私有属性

#  __private_attrs: 两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问.  
# 在类内部的方法中使用时 self.__private_attrs


class student:
    def __init__(self, name, age):
        self.n = name
        self.a = age
    def saying(self):
        print('我的名字是{0}, 年龄为{1}'.format(self.n, self.a))

student1 = student('bob',22)
student1.saying()

print('------------------------------------------------------------------------------------------------------')

class Test:
    def prt(self):
        print(self)
        print(self.__class__)   #self.__class__可访问实例对象的类

test1=Test()
test1.prt()


print('------------------------------------------------------------------------------------------------------')

class Student:
    def __init__(self, id, name, gender):
        self.id = id
        self.n = name
        self.g = gender
    def introduce(self):
        print('学生姓名：{1},学号：{0},性别：{2}'.format(self.id, self.n, self.g))

stu1=Student(123213124,'bob', 'male')
stu2=Student(123213125,'jim', 'male')
stu3=Student(123213126,'julia', 'female')
stu1.introduce()
stu2.introduce()
stu3.introduce()