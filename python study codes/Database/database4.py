
##操作SQLite数据
#插入数据
""" INSERT INTO 数据表 (字段1，字段2，...) VALUES (值1， 值2，...) """

#更新数据
""" UPDATE 数据表 SET 字段1 =值1 [,字段2=值2 ...] [WHERE限定条件] """

#删除数据
""" DELETE FROM 数据表 [WHERE 限定条件] """




##打开数据库test.db, 然后检测是否存在company表，如果没有，则新建company表，
# 使用INSERT INTO子句插入4条记录，最后用SELECT子句查询所有记录

import sqlite3                          #导入SQLite模块
conn = sqlite3.connect('test.db')       #连接到SQLite数据库，数据库文件是test.db
cursor = conn.cursor()                  #创建游标
try:                                    #创建数据表，如果存在则不创建，否则创建
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


#输出：[(1, '张三', 32, '北京', 20000.0), (2, '李四', 25, '上海', 15000.0), 
#       (3, '王五', 23, '广州', 20000.0), (4, '赵六', 25, '深州 ', 65000.0)]




##针对上例插入的4条记录，更新id为1的记录，修改该记录的salary字段值为25000.00，然后查询修改后的该条记录，并打印出来


import sqlite3                      #导入SQLite模块
conn = sqlite3.connect('test.db')   #连接到SQLite数据库，数据库文件是test.db
cursor = conn.cursor()
try:                                #更新记录
    cursor.execute("update company set salary = 25000.00 where id=1")
    conn.commit()                   #提交事务，执行更新操作
except:
    conn.rollback()                 #如果操作异常，则回滚事务
#查询记录
results = conn.execute("select id, name, address, salary from company where id=1")
for row in results:                 #打印记录
    print("id = ", row[0])
    print("name = ", row[1])
    print("address = ", row[2])
    print("salary = ", row[3], "\n")

cursor.close()
conn.close()


#输出：
# id =  1
# name =  张三
# address =  北京
# salary =  25000.0 


##使用DELETE语句删除company表中id为1的记录，然后查询所有记录，仅显示3条记录
import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
try:                        #删除记录
    cursor.execute("delete from company where id=1")
    conn.commit()
except:
    conn.rollback()
#查询记录
results = conn.execute("select id, name, address, salary from company")
for row in results:
    print("id = ", row[0])
    print("name = ", row[1])
    print("address = ", row[2])
    print("salary = ", row[3], "\n")
cursor.close()
conn.close()