## python 枚举

# http://www.ityouknow.com/python/2019/10/15/python-enum-033.html

# enum 是一组绑定到唯一常数值的符号名称，并且具备可迭代性和可比较性的特性。我们可以使用 enum 
# 创建具有良好定义的标识符，而不是直接使用魔法字符串或整数，也便于开发工程师的代码维护。


# 可以使用 class 语法创建一个枚举类型，方便我们进行读写，另外，
# 根据函数 API 的描述定义，我们可以创建一个 enum 的子类，如下

from enum import Enum

class HttpStatus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500


# 注意： 枚举属性值可以是任何东西: int, str 等。如果确切的值不重要，
# 您可以使用 auto 实例，并为您选择适当的值。如果您将auto与其他值混合，
# 则必须小心。 枚举类型中，不可以设置相同名称的name，可以有相同的 value。

## enum 自带属性 name 和 value

print('Menber:{}'.format(HttpStatus.OK))
print('Member name:{}'.format(HttpStatus.OK.name))
print('Member value:{}'.format(HttpStatus.OK.value))
print(repr(HttpStatus.OK))
print(str(HttpStatus.OK))
print(type(HttpStatus.OK))
print(isinstance(HttpStatus.OK, HttpStatus))


#枚举迭代  枚举支持迭代和遍历顺序

from enum import Enum, auto

#创建
class HttpStatus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500
    OTHER = auto.value

#迭代
for status in HttpStatus:
    print('{}:{}'.format(status.name, status.value))



##枚举成员与属性访问

#通过枚举value进行访问，访问需要使用元组()的形式
print(HttpStatus(200))

#通过枚举name进行访问，访问需要使用列表[]的形式
print(HttpStatus['OK'])

#将属性赋予另一个enum成员
number = HttpStatus.OK
print(number)


##枚举值唯一
# value 值是可以重复的，如不想枚举类中的值重复可以用装饰器@unique

from enum import Enum, unique

#创建
@unique
class HttpStatus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500
    OTHER = 200