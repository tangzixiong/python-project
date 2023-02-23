##SQLite 嵌入式数据库，一个数据库就是一个文件，不需要服务器环境的支持, python内置SQLite3,可直接使用SQLite

#创建test.db数据库文件，新建user数据表，表中包含id和name两个字段，插入记录，
#cursor.rowcount返回值为1，同时在当前目录新建test.db文件

# import sqlite3          #导入SQLite模块
# conn = sqlite3.connect('test.db')           #连接到SQLite数据库，数据库文件是test.db

# cursor = conn.cursor()                      #创建一个cursor
# try:
#     cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
#     #插入一条记录
#     cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
#     #通过rowcount获得插入的行数
#     conn.commit()                           #提交事务
# except:
#     conn.rollback()                         #回滚事务
# print(cursor.rowcount)                      #影响的行数
# cursor.close()                              #关闭cursor
# conn.close()                                #关闭connection



##从SQLite查询数据
# SELECT查询语句
""" SELECT 列名 FROM 表名 WHERE 限制条件 """

#在查询数据过程中，可以为SQL字符串传递变量。在SQL字符串中可以使用“？” 定义占位符，
# 在execute()方法的第二个参数中，可以以元组的格式传递一个或多个值

import sqlite3          #导入SQLite模块
conn = sqlite3.connect('Northwind_cn.db')       #连接到SQLite数据库
cursor = conn.cursor()                          #创建一个cursor
cursor.execute('select * from 产品 where ID =?', ('1',))        #执行查询语句
values = cursor.fetchall()                                      #使用fetchall获得结果集(list)
for i in values:
    print(i)
cursor.close()
conn.close    