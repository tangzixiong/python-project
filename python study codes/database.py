#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "shuke"
# Date: 2018/5/13

#### python操作MySQL模块

import pymysql           #导入PyMySQL模块
#打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="123456", database="python_test")

cursor = db.cursor()                  #使用cursor()方法创建一个游标对象cursor
cursor.execute("SELECT VERSION()")    #使用execute()方法执行SQL查询
data = cursor.fetchone()              #使用fetchone()方法获取单条数据
print("数据库的版本号: %s" % data)                              # 输出： 数据库的版本号: 8.0.32
db.close()                            #关闭数据库连接



##建立数据表
#连接数据库后，使用execute()方法为数据库创建数据表

#在python_test数据库中创建一个tb_new数据表， 包含id(主键)和user(用户名)两个字段

import pymysql

db = pymysql.connect(host="localhost", user="root", password="123456", database="python_test")
cursor = db.cursor()                                                  #使用cursor()方法创建一个游标对象cursor
cursor.execute("DROP TABLE IF EXISTS TB_NEW")                         #使用cursor()方法执行 SQL, 如果存在则删除
#使用预处理语句创建表
sql = """ CREATE TABLE tb_new (
        id INT NOT NULL AUTO_INCREMENT,
        user text,
        PRIMARY KEY (id)) """
cursor.execute(sql)                     #使用execu()方法执行SQL查询
cursor.close()                          #关闭游标对象
db.close()                              #关闭数据库连接


############################################################################
import pymysql

db = pymysql.connect(host="localhost", user="root", password="123456", database="python_test")
cursor = db.cursor()                                                #使用cursor()方法创建一个游标对象curser
#事务处理
try:                                                                #定义SQL插入语句
    sql = """ INSERT INTO tb_new(id, user) VALUES (10, 'test') """
    cursor.execute(sql)                                             #执行SQL语句
    db.commit()                                                     #提交事务，同步数据库数据
except:
    db.rollback()                                                   #如果发生错误则回滚事务
cursor.close()                                                      #关闭游标对象
db.close()                                                          #关闭数据库连接


##插入记录
#使用SQL的INSERT INTO语句实现
import pymysql

db = pymysql.connect(host="localhost", user="root", password='123456', database="python_test")
cursor = db.cursor()                                                    #使用cursor()方法创建一个游标对象curser
#定义SQL插入语句
sql = """ INSERT INTO tb_new(id, user) VALUES (1, "zhangsan") """       #定义SQL插入语句
try:
    cursor.execute(sql)
    db.commit()                                         #提交事务，同步数据库数据
except:
    db.rollback()                                       #若发生错误则回滚事务
cursor.close()                                          #关闭游标对象
db.close()                                              #关闭数据库连接


##使用executemany(sql, data)方法批量插入数据

import pymysql

bd = pymysql.connect(host="localhost", user="root", password="123456", database="python_test")
cursor = bd.cursor()                                    #使用cursor()方法创建一个游标对象curser

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