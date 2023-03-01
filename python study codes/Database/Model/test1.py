
##测试DBModel代码
from DBModel import DBTool
db = DBTool("test.db")
db("user", "name text, age int")
#插入一条记录
sql = 'insert into user (name, age) values(?, ?)'
while True:
    name = input('请输入名称：')
    age = input('请输入年龄：')
    ob = [(name, age)]
    T = db.exec(sql, ob)
    if T:
        print('插入成功！')
    else:
        print('插入失败！')
    go = input("是否继续插入(y/n): ")                #询问是否继续插入
    if go == "n" or go == "N":
        break                                       #跳出循环
    #查询插入的所有记录
    sql = 'select * from user'
    results = db.query(sql)                         #获取所有记录列表
    for row in results:
        print("name=%s, age=%s" % (row[0], row[1]))     #打印结果
    db.close()                                          #关闭对象