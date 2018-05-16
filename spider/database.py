#引入文件
import json
import pymysql


class SaveToDatabase(object):
    def __init__(self, host, user, passwd, db, port, charset):
        self.host    = host        # ip地址
        self.user    = user        # 用户名
        self.passwd  = passwd      # 密码
        self.db      = db          # 数据库
        #self.table   = table       # 表名
        self.port    = port        # 端口号
        self.charset = charset     # 字符集
        self.connect = None        # 数据库连接
        self.cursor  = None        # 数据库光标

    def ConnectDatabase(self):
        # 打开数据库连接
        self.connect = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, port=self.port, charset=self.charset)
        # 使用cursor()方法获取操作游标 
        self.cursor = self.connect.cursor()

    #该方法用于处理数据
    def InsertData(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.connect.commit()
        except Exception as e:
            # 如果发生错误则回滚
            self.connect.rollback()
            print(e)
            return False

        return True

    def SelectData(self, sql):
        results = None
        try:
           # 执行SQL语句
           self.cursor.execute(sql)
           # 获取所有记录列表
           results = self.cursor.fetchall()
           
        except:
           print("Error: unable to fecth data")

        return results


    def CloseDatabase(self):
        # 关闭数据库连接
        self.connect.close()