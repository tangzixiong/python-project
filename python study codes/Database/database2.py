
##使用executemany(sql, data)方法批量插入数据

import pymysql

db = pymysql.connect(host="localhost", user="root", password="123456", database="python_test")
cursor = db.cursor()                                    #使用cursor()方法创建一个游标对象curser

sql = 'insert tb_new(id, user) values(%s, %s)'      #定义要执行的SQL语句
data = [
    (2, 'lisi'),
    (3, 'wangwu'),
    (4, 'zhaoliu')
]
try:
    cursor.executemany(sql, data)
    db.commit()
except:
    db.rollback()
cursor.close()
db.close()


##查询记录， 主要使用SQL的SELECT语句实现，
#使用cursor对象的execute()方法执行查询后，再通过以下4个方法读取数据
#fetchall(): 获取结果集中的所有行
#fetchmany(size=None): 获取结果集中的size条记录。如果size大于结果集中行的数量，则返回cursor.arraysize条记录
#fetchone(): 获取结果集中下一行记录
#rowcount: 只读属性，返回执行execute()方法后影响的行数



##查询tb_new表中id字段大于1的所有数据
import pymysql                              #导入pymysql模块

db = pymysql.connect(host="localhost", user="root", password="123456", database="python_test")
cursor = db.cursor()                        #使用cursor()方法创建一个游标对象cursor
# SQL 查询语句
sql = "SELECT * FROM tb_new WHERE id > %s" % (1)
try:
    cursor.execute(sql)                         #执行SQL语句
    results = cursor.fetchall()                 #获取所有记录列表
    for row in results:
        id = row[0]
        user = row[1]
        print("id=%s, user=%s" %(id, user))     #打印结果
except:
    print("Error: unable to fetch data")
db.close()                                      #关闭数据库连接




##更新记录， 主要使用SQL的UPDATE语句实现

#将tb_new表中id为2的 user 字段修改为new_name
import pymysql

db = pymysql.connect(host="localhost", user="root", password="123456", database="python_test")
cursor = db.cursor()
# SQL更新语句
sql = "UPDATE tb_new SET user = 'new_name' WHERE id = 2"
try:
    cursor.execute(sql)             #执行SQL语句
    db.commit()                     #提交事务，同步数据库数据 
except:
    db.rollback()                   #发生错误时回滚事务
db.close()                          #关闭数据库连接


##删除记录  主要使用SQL的 DELETE FROM 语句实现

#将tb_new表中id为2的记录删除
import pymysql
db = pymysql.connect(host="localhost", user="root", password="123456", database="python_test")
cursor = db.cursor()
sql = "DELETE FROM tb_new WHERE id = 2"     # SQL 删除语句
try:
    cursor.execute(sql)                     #执行SQL语句
    db.commit()                             #提交事务
except:
    db.rollback()                           #发生错误时回滚事务
db.close()

