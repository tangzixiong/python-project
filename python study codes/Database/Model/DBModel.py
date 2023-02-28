
#在DBModel.py文件中导入SQLite模块，定义DBTool类，在该类中封装SQLite数据库操作的相关函数，
#包括创建指定的数据库和数据表，以及数据的常规操作，如插入、更新、删除、查询等，
#表的结构以SQL字符串的格式指定
""" "字段名  类型， 字段名 类型，..." """

import sqlite3              #导入SQLite模块
class DBTool(object):
    def __init__(self, name):          #初始化函数
        """
        创建数据库连接
        :param name: 数据库文件的路径和名称
        """
        try:
            self.conn = sqlite3.connect(name)           #创建或打开数据库
            self.curs = self.conn.cursor()              #获取游标对象
        except:
            print('创建或打开数据库失败')
            return None