#定义普通方法、类方法和静态方法

class Test():
    name = 'Test'
    def __init__(self,name):
        self.name=name

    def ord_func(self):
        """ 普通方法，至少包含一个self参数 """
        print('普通方法')
        print(self.name)

    @classmethod
    def class_func(cls):
        """ 类方法，至少包含一个cls参数 """
        print('类方法')
        print(cls.name)

    @staticmethod
    def static_func():
        """ 静态方法，无默认参数 """
        print('静态方法')

#print(name)
f = Test('test')                #实例化类
f.ord_func()                    #实例对象调用普通方法
f.class_func()                  #实例对象调用类方法
f.static_func()                 #实例对象调用静态方法
Test.class_func()               #类对象调用类方法
Test.static_func()              #类对象调用静态方法


print('--------------------------------------------1----------------------------------------------------------')

#实例对象使用类方法修改静态字段的值

class People():
    country = '中国'

    @classmethod
    def get(cls):
        return cls.country
    @classmethod
    def set(cls, country):
        cls.country = country

p = People()        #实例化类
print(p.get())      #通过实例对象引用
print(People.get()) #通过类对象引用
p.set('美国')       #通过实例对象调用
print(p.get())      #通过实例对象引用类方法

print('--------------------------------------------2----------------------------------------------------------')

class People():
    country = '中国'
    @staticmethod
    def get():
        return People.country
    
p = People()
print(p.get())
print(People.get())        


print('---------------------------------------------3---------------------------------------------------------')

#属性
class Test:
    _name = 'test'              #静态字段
    def get_name(self):         #普通方法
        return self._name       #返回_name字段值
    #定义属性
    @property
    def name(self):             #属性
        return self._name       #返回_name字段值
    
obj = Test()
print(obj.get_name())           #调用方法
print(obj.name)                 #读取属性




print('----------------------------------------------4--------------------------------------------------------')

#设计一个数据库分页显示功能模块，能根据用户请求的当前页数以及预定的每页显示的记录数计算将要显示的从第m条到第n条的记录起止数

class Pager:
    def __init__(self, current_page):
        self.current_page = current_page
        self.per_items = 10
    @property
    def start(self):
        val = (self.current_page-1) * self.per_items
        return val
    @property
    def end(self):
        val = self.current_page * self.per_items
        return val

p = Pager(3)
print(p.start)   # 调用属性函数时，不需要使用小括号
print(p.end)

print('------------------------------------------------5------------------------------------------------------')

#属性的访问方式，读、写、删； 对应的修饰器为 @property、 @方法名.setter、 @方法名.deleter

class Goods(object):
    def __init__(self, price, discount=1):
        self.orig_price = price
        self.disc = discount
    @property
    def price(self):                        #读取属性
        new_price = self.orig_price * self.disc
        return new_price
    @price.setter
    def price(self, value):                #写入属性
        self.orig_price = value 
    @price.deleter
    def price(self):                       #删除属性
        del self.orig_price


g = Goods(8,0.88)
print(g.price)
g.price=10
del g.price
print(g.price)       #不存在，将抛出异常

print('------------------------------------------------6------------------------------------------------------')

#property()构造函数可把属性操作的函数绑定到字段上，可快速定义属性
#class property([fget[, fset[, fdel[, doc]]]])
        #fget:获取属性值的普通方法
        #fset:设置属性值的普通方法
        #fdel:删除属性值的普通方法
        #doc:属性描述信息

class Goods:
    def __init__(self, price, discount):
        self.orig_price = price
        self.disc = discount
    def get_price(self):
        new_price = self.orig_price * self.disc
        return new_price
    def set_price(self, value):
        self.orig_price = value
    def del_price(self):
        del self.orig_price

    #构造price属性
    price = property(get_price, set_price, del_price, "可读，可写，可删属性：商品价格")

obj = Goods(100,0.88)
print(obj.price)                        #obj.price将触发get_price方法， 
obj.price = 200                         #obj.price=200将出发set_price方法
del obj.price                           #del obj.price将触发del_price方法， 
# print(obj.price) #不存在，将抛出异常

print('---------------------------------------------7---------------------------------------------------------')

class Test:
    def __init__(self):             #初始化函数
        self.a='公有字段'
        self.__b = "私有字段"
    def get(self):                  #公共方法
        return self.__b             
    
test = Test()
print(test.a)                       #直接访问公有字段
print(test.get())                   #间接访问私有字段
# print(test.__b)                   #直接访问私有字段，将抛出异常

print(test._Test__b)                #强制访问私有字段：对象._类__属性名。    输出为私有字段

