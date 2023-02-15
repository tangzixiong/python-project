##设置一个MyMath类，能实现简单的加减乘除运算
""" 
class MyMath:                       #定义MyMath类
    def __init__(self, a, b):       #初始化类
        self.a = a
        self.b = b
    def addition(self):         
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        if self.b == 0:
            print('除数不能为0')
        else:
            return self.a / self.b
while True:                         #无限次使用计算器
    a = int(input('参数a:'))
    b = int(input('参数b:'))
    myMath = MyMath(a, b)
    print('加法结果:', myMath.addition())
    print('减法结果:', myMath.subtraction())
    print('乘法结果:',myMath.multiplication())
    if myMath.division() != None:                   #除数不为0时，返回值不为None
        print('除法结果:',myMath.division())
    flag = input('是否退出运算[y/n]:')
    if flag == 'y':
        break
 """

print('-----------------------------------1----------------------------------------------')

class Circle:                           #圆类
    def __init__(self, x, y, r):        #初始化类
        self.x = x
        self.y = y
        self.r = r
    def get_position(self):             #获取圆位置函数
        return (self.x, self.y)         #位置信息以元组方式返回
    def set_position(self, x, y):       #设置圆位置函数
        self.x = x
        self.y = y
    def get_area(self):                 #圆面计算函数
        return 3.14 * self.r**2
    def get_circumference(self):        #圆周长计算函数
        return 2 * 3.14 * self.r

circle = Circle(2, 4, 4)                #实例化圆类
area = circle.get_area()                #计算圆的面积
circumference = circle.get_circumference()      #计算圆的周长
print('圆的面积:', area)
print('圆的周长:', circumference)
print('圆的初始位置:', circle.get_position())
circle.set_position(3, 4)                       #修改圆的位置
print('修改后圆的位置:', circle.get_position())


print('-----------------------------------2----------------------------------------------')

##设计鞋类

class Shoes:                                #定义鞋子类
    numbers = 0                             #静态字段
    def __init__(self, name, brand):        #初始化类
        self.name = name
        self.brand = brand
        Shoes.numbers += 1                  #初始化类时，累加鞋子数量
    def useless(self):                      #定义没用的鞋子方法
        Shoes.numbers -= 1                  #数量减1
        if Shoes.numbers == 0:
            print('{} was the last one'.format(self.name))      #打印最后一双鞋的名字
        else:
            print('you have {:d} shoes'.format(Shoes.numbers))    #打印鞋子的数量
    def print_shoes(self):                                        #定义鞋子的详细方法
        print('you got {:s} {:s}'.format(self.name, self.brand))
    @classmethod                           #声明类方法
    def how_many(cls):                     #定义鞋子的数量方法
        print('you have {:d} shoes.'.format(cls.numbers))

shoes1 = Shoes('三叶草','ADIDAS')          #实例化类
shoes1.print_shoes()                      #打印鞋子信息
Shoes.how_many()                          #打印鞋子数量

shoes2 = Shoes('AJ', 'NIKE')
shoes2.print_shoes()
Shoes.how_many()

shoes1.useless()
shoes2.useless()
Shoes.how_many()


print('----------------------------------------3----------------------------------------------')
##自行车类
class Bike:
    def __init__(self, brand, color):
        self.oral_brand = brand
        self.oral_color = color
    @property                       #属性
    def brand(self):
        return self.oral_brand      #返回字段值
    @brand.setter
    def brand(self, b):
        self.oral_brand = b         #设置字段值
    @property                       #属性
    def color(self):
        return self.oral_color      #返回字段值
    @color.setter
    def color(self, c):
        self.oral_color = c         #设置字段值
    def riding(self):               #定义骑行方法
        print('自行车可以骑行')
class Folding_Bike(Bike):           #定义折叠自行车类
    def __init__(self, brand, color):       #初始化函数
        super().__init__(brand, color)      #调用父类方法
    def riding(self):                       #重写父类方法
        print('折叠自行车:{}{}可以折叠'.format(self.color, self.brand))
class Electric_Bike(Bike):                  #定义电动车类
    def __init__(self, brand, color, battery):      #初始化函数
        super().__init__(brand, color)              #调用父类方法
        self.oral_battery = battery
    @property                                       #属性
    def battery(self):
        return self.oral_battery                    #返回字段值
    @battery.setter
    def battery(self, b):
        self.oral_battery = b                       #设置字段值
    def riding(self):                               #重写父类方法
        print('电动车：{}{}使用{}电池'.format(self.color, self.brand, self.battery))

f_bike = Folding_Bike('捷安特', '白色')             #实例化折叠自行车类
f_bike.riding()
f_bike.color = '黑色'                               #设置字段值
f_bike.riding()
e_bike = Electric_Bike('小刀', '蓝色', '55V20AH')   #实例化电动车类
e_bike.riding()
e_bike.battery = '60V20AH'                          #设置字段值
e_bike.riding()

print('----------------------------------------4----------------------------------------------')

##设计矩形类

class Rectangle:                                            #定义矩形类
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):                                         #定义面积方法
        return self.width * self.height
    def perimeter(self):                                    #定义周长方法
        return 2 * (self.width + self.height)
class PlainRectangle(Rectangle):                            #定义有位置参数的矩形
    def __init__(self, width, height, startX, startY):
        super().__init__(width, height)                     #调用父类方法  Rectangle.__init__(self, width, height)
        self.startX = startX
        self.startY = startY
    def isInside(self, x, y):                               #定义点与矩形位置方法
        if (x>=self.startX and x<=(self.startX + self.width) and
(y>=self.startY and y<=(self.startY+self.height))):         #点在矩形上的条件
            return True
        else:
            return False
        
plainRectangle = PlainRectangle(10, 5, 10, 10)
print('矩形的面积:', plainRectangle.area())
print('矩形的周长:', plainRectangle.perimeter())
if plainRectangle.isInside(15, 11):
    print('点在矩形内')
else:
    print('点不在矩形内')

print('----------------------------------------5----------------------------------------------')

#创建一个返回数字的迭代器，初始值为 1，逐步递增1 
class Add:
    def __iter__(self):         #魔术函数，当迭代器初始化时调用
        self.a = 1
        return self
    def __next__(self):         #魔术函数，当调用next()函数时调用
        x = self.a              #临时缓存递增变量值
        self.a +=1              #递增变量a的值
        return x                #返回递增之前的值
    
add = Add()                     #实例化Add类型
myiter = iter(add)              #调用iter()函数，初始化为迭代器对象
print(next(myiter))             #调用next()函数
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(add.__iter__())
    
print('----------------------------------------6----------------------------------------------')

##StopIteration异常用于标识迭代的完成，防止出现无限循环
class Add:
    def __iter__(self):          #魔术函数，当迭代器初始化时调用
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a          #临时缓存递增变量值
            self.a +=1          #递增变量a的值
            return x            #返回递增之前的值
        else:
            raise StopIteration     #抛出异常

add = Add()
myiter = iter(add)
for x in myiter:
    print(x, end=' ')

print('----------------------------------------7----------------------------------------------')


##使用生成器推导斐波那契数列

def fib(max):               #生成器函数
    n, a, b = 0, 0, 1       #初始化
    while n < max:
        yield b             #返回变量b的值
        a, b = b, a+b       #多重赋值
        n = n + 1           #递增值
    return 'done'

g = fib(6)                  #创建生成器大小
while True:
    try:
        x = next(g)         #读取下一个元素的值
        print(x)
    except StopIteration as e:      #不捕获异常
        print(e.value)
        break


print('----------------------------------------8----------------------------------------------')

