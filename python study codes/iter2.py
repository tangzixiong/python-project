#创建一个返回数字的迭代器，初始值为 1，逐步递增 1

## isinstance(): 判断一个对象是否是某个类的实例
## python————迭代器：http://www.ityouknow.com/python/2019/09/21/python-iterator-019.html

class MyNumbers:
    def __iter__(self): 
        self.a = 1           # iter() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 next() 方法并通过 StopIteration 异常标识迭代的完成
        return self

    def __next__(self):      # next() 方法会返回下一个迭代器对象
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass) 

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print('------------------------------------------1------------------------------------------------------------')


###如果一个类实现了下面两个方法：
#__iter__():返回self, 即迭代器自身
#__next__():返回下一个可用的元素，当没有元素时抛出StopIteration异常
#那么它的实例就是一个迭代器(Iterator), 迭代器是一个可以从可迭代的对象中取出元素，且能记住遍历位置的对象.

#定义一个可迭代对象类、一个迭代器类，然后把它们捆绑在一起，实现根据指定的上边界，迭代显示一个非负数字列表。

class MyList(object):               #可迭代对象类
    def __init__(self, num):        #初始化
        self.data = num             #设置可迭代的上边界
    def __iter__(self):             #迭代器
        return MyListIterator(self.data)    #返回该可迭代对象的迭代器类的实例
    
class MyListIterator(object):           #迭代器类，供MyList可迭代对象专用
    def __init__(self, data):
        self.data = data                   #初始可迭代的上边界
        self.now = 0                    #当前迭代值，初始为0
    def __iter__(self):                 
        return self                     #返回迭代器类的实例
    
    def __next__(self):                 #迭代器类必须实现的方法，获取下一个元素
        while self.now < self.data:
            self.now +=1
            return self.now - 1         #返回当前迭代值
        raise StopIteration             #超出上边界，抛出异常
    
my_list = MyList(5)                     #创建一个可迭代的对象
print( type(my_list) )                  #返回可迭代对象的类型  <class '__main__.MyList'>
my_list_iter = iter(my_list)            #获取该对象的迭代器
print( type(my_list_iter))              #返回可迭代对象的类型  <class '__main__.MyListIterator'>
for i in my_list:                       #迭代可迭代对象my_list
    print( i )


print('------------------------------------------2------------------------------------------------------------')

list = [1,2,3,4]
it = iter(list)
print(next(it), end=' ')
print(next(it), end=' ')
print(next(it), end=' ')
print(next(it), end=' ')

for i in iter(list):
    print(i, end=' ')

print('------------------------------------------3------------------------------------------------------------')


from collections.abc import Iterable            #导入Iterable类型
from collections.abc import Iterator            #导入Iterator类型
list = [1, 2, 3, 4]                             #定义列表
it = iter(list)                                 #创建迭代器对象
print(isinstance(list, Iterable))               
print(isinstance(it, Iterable))
print(isinstance(list, Iterator))
print(isinstance(it, Iterator))