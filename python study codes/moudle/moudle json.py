## JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式
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