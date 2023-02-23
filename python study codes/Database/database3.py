##SQLite 嵌入式数据库，一个数据库就是一个文件，不需要服务器环境的支持, python内置SQLite3,可直接使用SQLite

#创建test.db数据库文件，新建user数据表，表中包含id和name两个字段，插入记录，
#cursor.rowcount返回值为1，同时在当前目录新建test.db文件

import sqlite3          #导入SQLite模块
conn = sqlite3.connect('test.db')           #连接到SQLite数据库，数据库文件是test.db

cursor = conn.cursor()                      #创建一个cursor
try:
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
    #插入一条记录
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    #通过rowcount获得插入的行数
    conn.commit()                           #提交事务
except:
    conn.rollback()                         #回滚事务
print(cursor.rowcount)                      #影响的行数
cursor.close()                              #关闭cursor
conn.close()                                #关闭connection
