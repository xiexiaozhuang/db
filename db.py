# -*- coding:utf-8 -*-
# author xxz
#引入pymysql
import pymysql
#创建类
class Db:
    def __init__(self,host='127.0.0.1',user='root',mima='root',
                 dbname='',charset='utf8'):
        self.host=host
        self.user=user
        self.mima=mima
        self.dbname=dbname
        self.charset=charset
    def open(self):
        #连接数据库
        self.db=pymysql.connect(host=self.host,user=self.user,password=self.mima,
                                database=self.dbname,charset=self.charset)
        #创建游标
        self.link=self.db.cursor()
    def close(self):
        #关闭游标
        self.link.close()
        #关闭数据库
        self.db.close()
    def readall(self,sql):
        try:
            self.open()
            #执行sql语句
            self.link.execute(sql)
        except Exception as e:
            print(e)
            self.close()
            return False
        else:
            #读取所有数据
            data=self.link.fetchall()
            self.close()
            return data

