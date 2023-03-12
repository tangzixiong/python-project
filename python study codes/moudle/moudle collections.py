##collections 模块

# http://www.ityouknow.com/python/2019/10/11/python-collections-030.html

# collections 是 python 的内置模块，提供了很多方便且高性能的
# 关于集合的操作，掌握这些知识有助于提高代码的性能和可读性。

## namedtuple() 返回一个新的元组子类，且规定了元组的元素的个数，
# 同时除了使用下标获取元素之外，还可以通过属性直接获取。

from collections import namedtuple
User = namedtuple("User",["name", "age", "weight"])
user = User("admin", "20", "60")
name, age, weight = user
print(user[0])
print(name, age, weight)
print(user.name, user.age, user.weight)


##将序列直接转换为新的tuple对象
user = ["root", 32, 65]
user = User._make(user)
print(user)
#输出 User(name='root', age=32, weight=65)

#返回一个dict
user = User("admin", 20, 60)
print(user._asdict())


##ChainMap()  可以将多个字典集合到一个字典中去，对外提供一个统一的视图。
# 该操作并是不将所有字典做了一次拷贝，实际上是在多个字典的上层又进行了一次封装而已

from collections import ChainMap

user1 = {"name":"admin", "age":"20"}
user2 = {"name":"root", "weight":65}
users = ChainMap(user1, user2)
print(users.maps)

users.maps[0]["name"] = "tiger"
print(users.maps)

for key, value in users.items():
    print(key, value)


#如果 ChainMap() 中的多个字典有重复 key，查看的时候可以看到所有的 key，但遍历
# 的时候却只会遍历 key 第一次出现的位置，其余的忽略。同时，我们可以通过返回的新
# 的视图来更新原来的的字典数据。进一步验证了该操作不是做的拷贝，而是直接指向原字典。


## deque()  dqueue 是 ”double-ended queue” 的简称，是一种类似列表(list)的容器，
#  实现了在两端快速添加(append)和弹出(pop)操作。大大加快了遍历速度

from collections import deque
q = deque([1,2,3])
q.append('4')
q.appendleft('0')
print(q)
print(q.popleft())


## Counter 可以简单理解为一个计数器，可以统计每个元素出现的次数，
# 同样 Counter() 是需要接受一个可迭代的对象的

from  collections import  Counter
animals = ["cat", "dog", "cat", "bird", "horse", "tiger", "horse", "cat"]
animals_counter = Counter(animals)
print(animals_counter)
print(animals_counter.most_common(2))

# Counter({'cat':3, 'horse':2, 'dog':1, 'bird':1, 'tiger':1})
# [('cat', 3), ('horse', 2)]

#其实一个 Counter 就是一个字典，其额外提供的 most_common() 函数通常用于求 Top k 问题。



##OrderedDict 是字典的子类，保证了元素的插入顺序
# 算法上， OrderedDict 可以比 dict 更好地处理频繁的重新排序操作。
# 在跟踪最近的访问这种场景（例如在 LRU cache）下非常适用。OrderedDict类
# 有一个 move_to_end() 方法，可以有效地将元素移动到任一端。


from collections import OrderedDict

user = OrderedDict()
user["name"] = "admin"
user["age"] = 23
user["weight"] = 65
print(user)
user.move_to_end("name")
print(user)
user.move_to_end("name", last = False)
print(user)


##defaultdict  是内置 dict 类的子类。它实现了当 key 不存在
# 是返回默认值的功能，除此之外，与内置 dict 功能完全一样

from collections import defaultdict

default_dict = defaultdict(int)
default_dict["x"] = 10
print(default_dict["x"])
print(default_dict["y"])