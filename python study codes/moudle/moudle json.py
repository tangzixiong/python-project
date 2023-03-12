### json & pickle

# http://www.ityouknow.com/python/2019/10/18/python-json&pickle-034.html

# 日常开发中，对数据进行序列化和反序列化是常见的数据操作，Python提供了两个模块方便开发者实现数据的序列化操作，即 json 模块和 pickle 模块。

# 这两个模块主要区别如下：
    # json 是一个文本序列化格式，而 pickle 是一个二进制序列化格式；
    # json 是我们可以直观阅读的，而 pickle 不可以；
    # json 是可互操作的，在 Python 系统之外广泛使用，而 pickle 则是 Python 专用的；
    # 默认情况下，json 只能表示 Python 内置类型的子集，不能表示自定义的类；但 pickle 可以表示大量的 Python 数据类型。






## JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式, 由于其具有
# 传输数据量小、数据格式易解析等特点，它被广泛应用于各系统之间的交互操作
    ## dumps(): 将Python对象序列化为JSON字符串表示
    ## dump(): 将Python对象序列化为JSON字符串,然后保存到文件中
    ## loads(): 把JSON格式的字符串反序列化为Python对象
    ## load(): 读取文件内容， 然后反序列化为Python对象



##将字典对象序列化为JSON字符串， 再反序化为Python的字典类型的对象

import json                             #导入JSON模块
a = {"name":"Tom", "age":23}            #定义字典对象
b = json.dumps(a)                       #将字典对象序列化JSON字符串
print(b)                                #打印JSON字符串
c = json.loads(b)                       #将JSON字符串反序列化为字典对象
print(c['name'])


print('------------------------------------1-----------------------------------------')

#将字典对象序列化为字符串，然后使用dump()方法保存到test.json文件中，再使用load()方法从test.json文件中读取字符串，并转换为字典对象

import json
a = {"name":"Tom", "age":"23"}                              #定义字典对象
with open("moudle.json", "w", encoding='utf-8') as f:
    # indent 表示格式化保存字符串，默认为None, 小于0为零个空格
    json.dump(a, f, indent=4)                               #将字典对象序列化为字符串
                                                            #然后保存到test.json文件中
    # f.write(json.dumps(a, indent=4))                      #与json.dump()效果一样
with open("moudle.json", "r", encoding='utf-8') as f:
    b = json.load(f)                                        #从test.json中读取内容，然后把内容转换为Python对象

    f.seek(0)                           #重新把文件指针移到文件开头
    c = json.loads(f.read())            #与json.load(f)执行效果一样
print(b)
print(c)



########################################################################################


# python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。


""" 
pickle.dump(obj, file, [,protocol])
"""

#有了 pickle 这个对象, 就能对 file 以读取的形式打开:
        
    # x = pickle.load(file)       #从 file 中读取一个字符串，并将它重构为原来的python对象。


""" 
#!/usr/bin/python3
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close() """







#!/usr/bin/python3
import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()