
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
    def __call__(self, table, fields):                  #调用实例对象
        """
        创建数据表
        :param table: 数据表的名称
        :param fields: SQL字符串,字段列表 
        """
        try:                            #判断是否存在指定的表，否则创建表和结构
            creat_tb= 'create table if not exists %s ( %s )' % (table, fields)
            self.conn.execute(create_tb)
        except Exception as e:
            print('创建表失败')
            print('错误类型：', e)
    def exec(self, sql, args=[]):
        """
        数据库基本操作，可执行插入、修改、删除操作
        :param sql: SQL字符串
        :param args: SQL字符串的参数列表 
        :return: 返回操作成功与否
        """
        try:                            #如果参数args为嵌套序列，则批量处理
            if (isinstance(args, (list, tuple)) and len(args)>0 and
                isinstance(args[0],(list, tuple, dict)) and len(args[0]>0)):
                self.curs.executemany(sql, args)
            else:                       #否则执行单个SQL字符串
                self.curs.execute(sql, args)
            i = self.conn.total_changes         #被修改、插入或删除的数据总行数
            self.conn.commit()                  #提交事务
        except Exception as e:
            print('错误类型：', e)
            self.conn.rollback()                #回滚事务
            return False
        if i > 0:                               #根据操作反馈结果，返回布尔值
            return True
        else:
            return False
    def query(self, sql, args=[]):
        """
        数据查询
        :param sql: SQL字符串
        :param args: SQL字符串的参数列表
        :return: 返回查询结果 
        """
        result = self.curs.execute(sql, args)       #执行查询
        return result                               #返回查询结果对象
    def close(self):
        """
        关闭连接
        :return: 
        """
        self.curs.close()                           #关闭游标对象
        self.conn.close()                       #关闭数据库连接