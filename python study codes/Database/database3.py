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

# import sqlite3          #导入SQLite模块
# conn = sqlite3.connect('Northwind_cn.db')       #连接到SQLite数据库
# cursor = conn.cursor()                          #创建一个cursor
# cursor.execute('select * from 产品 where ID =?', ('1',))        #执行查询语句
# values = cursor.fetchall()                                      #使用fetchall获得结果集(list)
# for i in values:
#     print(i)
# cursor.close()
# conn.close()


#比较查询
#一般要使用where限制条件
""" SELECT 产品名称，列出价格，FROM 产品 WHERE 列出价格>50 """

#多条件查询
#使用关键字AND和OR可以筛选满足一个或同时满足多个限定条件
""" SELECT * FROM 产品 WHERE 列出价格>=30 AND 标准成本<10"""

#范围查询
#使用关键字IN和NOT IN可以筛选在或者不在某个范围内的结果
""" SELECT * FROM 产品 WHERE 类别 NOT IN ('调味品', '干果和坚果') """

#模糊查询
#使用关键字LIKE可以实现模糊查询，还可使用通配符代表未知字符，其中“—”代表一个未指定字符，“%”代表若干个未指定字符
""" SELECT * FROM 产品 WHERE 产品名称 LIKE '%肉%'"""

#结果排序
#使用ORDER BY关键字可以排序查询的结果集， 关键字ASC和DESC可以指定升序或降序排序
""" SELECT * FROM 产品 WHERE 类别 = '调味品' ORDER BY 列出价格 DESC"""



###在SQL语句中可以使用占位符，SQLite3模块支持两种占位符：问号(?)和命名占位符
""" 
#以问号格式定义占位符，传值时可以使用序列对象
cursor.execute("SELECT * FROM 产品 WHERE
        列出价格>=? AND 标准成本<?", (30,20))
#以命名格式定义占位符(名字占位符前面要加：前缀)，传值时必须使用字典进行映射
cursor.execute("SELECT * FROM 产品 WHERE
            列出价格>=:price AND 标准成本<:cost ", {"price":30, "cost":20})
"""


##操作SQLite数据
#插入数据
""" INSERT INTO 数据表 (字段1，字段2，...) VALUES (值1， 值2，...) """

#更新数据
""" UPDATE 数据表 SET 字段1 =值1 [,字段2=值2 ...] [WHERE限定条件] """

#删除数据
""" DELETE FROM 数据表 [WHERE 限定条件] """




##打开数据库test.db, 然后检测是否存在company表，如果没有，则新建company表，
# 使用INSERT INTO子句插入4条记录，最后用SELECT子句查询所有记录

import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()                  #创建游标
try:
    cursor.execute(""" creat table if not exists company
        (id int primary key     not null,
        name        text    not null,
        age         int     not null,
        address     char(50),
        salary      real);""")
except:
    pass
try:                                #插入4条记录
    cursor.execute("insert into company (id, name, age, address, salary) values (1,'张三', 32, '北京', 20000.00)")
    cursor.execute("insert into company (id, name, age, address, salary) values (2,'李四', 25, '上海', 15000.00)")
    cursor.execute("insert into company (id, name, age, address, salary) values (3,'王五', 23, '广州', 20000.00)")
    cursor.execute("insert into company (id, name, age, address, salary) values (4,'赵六', 25, '深圳', 65000.00)")
    conn.commit()           #提交事务，完成数据写入操作
except:
    conn.rollback()
cursor.execute('select * from company')         #查询所有数据
values = cursor.fetchall()                      #使用fetchall获得结果集（list)
print(values)
cursor.close()
conn.close()