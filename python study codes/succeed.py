##继承
#新建的类可以继承自一个或多个类，被继承的类称为父类、基类、或超类，新建的类称为子类或派生类
""" class 子类(基类列表):
        帮助信息(可选)
        类主体
"""

class Parent:                       #定义父类
    name = '父类'                   #身份标识字段
    def get(self):                  #方法
        return self.name
class Son1(Parent):                 #定义子类1，继承自Parent
    name = '子类1'
class Son2(Parent):                 #定义子类2，继承自Parent
    name = '子类2'

son1 = Son1()                       #实例化子类1
print(son1.get())                   #输出为子类1
son2 = Son2()                       #实例化子类2
print(son2.get())                   #输出为子类2

print('------------------------------------------1-----------------------------------------------')

class Parent1:
    name = '父类1'
    def get(self):
        return self.name
class Parent2:
    name = '父类2'
    def set(self, val):
         self.name = val
class Son(Parent1,Parent2):         #定义子类，继承自parent1和parent2
    name = '子类'

son = Son()                        #实例化子类
print(son.get())                   #调用get()方法，输出为子类
son.set('test')                    #调用set()方法，修改name属性
print(son.get())                   #调用get()方法，输出为test



print('------------------------------------------2-----------------------------------------------')

##类的组合：在一个类中使用另一个类的对象作为数据属性

class Teacher:                              #教师类
    def __init__(self, name, gender, course):
        self.name = name
        self.gender = gender
        self.course = course
class Course:                               #课程类
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

course_obj = Course('Python', 15800, '5months')     #新建课程对象

#教师与课程的关系

t_c = Teacher('egon', 'male', course_obj)           #新建教师实例，组合课程对象
print(t_c.course.name)
print(t_c.course.price)

print('------------------------------------------3-----------------------------------------------')

class BirthDate:                                    #生日类
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
class Course:                                       #课程类
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period
class Teacher:                                      #教师类
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def teach(self):
        print('teaching')
class Professor(Teacher):                           #教授类
    def __init__(self, name, gender, birth, course):
        Teacher.__init__(self, name, gender)        #调用父类方法，初始化参数
                                                    #也可使用super().__init__(name, gender)
#通常使用super(), 省略self参数， 利于维护， 因为super()指代父类，而父类可能会改变

        self.birth = birth
        self.course = course

p1 = Professor('egon', 'male', 
               BirthDate('1998','1','20'),
               Course('Python','58000', '4 months'))
print(p1.birth.year, p1.birth.month, p1.birth.day)
print(p1.course.name, p1.course.price, p1.course.period)


print('------------------------------------------4-----------------------------------------------')
#方法重写与扩展
class Bird:                            # Bird类，基类
    def eat(self):                     # eat()方法
        print('Bird, 吃东西...')
class SongBird(Bird):                  # SongBird类， 派生类
    def eat(self):                     # 重写基类eat()方法
        print('SongBird, 吃东西...')
    def song(self):                    # 扩展song()方法
        print('SongBird, 唱歌...')

bird = Bird()
songBird = SongBird()
bird.eat()
songBird.eat()
songBird.song()


print('------------------------------------------5-----------------------------------------------')



class Fruit:                            #基类
    color = '绿色'                      #字段
    def harvest(self, color):           #方法
        print(f"现是{color}")
        print(f"初是{Fruit.color}")

class Apple(Fruit):                    #派生类1
    color = "红色"                     #字段
    def __init__(self):                #方法
        print("苹果")

class Orange(Fruit):                #派生类1
    color = "橙色"                  #字段
    def __init__(self):
        print("\n橘子")
    def harvest(self, color):     #重写harvest()方法
        print(f"现是{color}")
        print(f"初是{Fruit.color}")

apple = Apple()                     #实例化Apple类
apple.harvest(apple.color)          #在Apple中调用harvest()方法，并将Apple()的color变量传入

orange = Orange()                   #实例化Orange类
orange.harvest(orange.color)        #在Orange中调用harvest()方法，并将Orange()的color的变量传入


print('------------------------------------------6-----------------------------------------------')


