"""
==============================
Author:A
Time:2020/4/9
E-mail:1066453201@qq.com
==============================
"""
"""
查询
"""

import pymysql
from config  import user_config


class DB:
    def __init__(self):
        self.conn = pymysql.connect(
                                    host = user_config.host,
                                    port = user_config.port,
                                    user = user_config.user,
                                    password = user_config.pwd,
                                    database = user_config.database,
                                    charset = user_config.charset,
                                    cursorclass= pymysql.cursors.DictCursor
                                    )
        # 创造一个游标
        self.cur = self.conn.cursor()


    def find_one(self,sql):
        """获取查询出来的第一条数据"""
        # 执行查询语句
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def find_all(self, sql):
        """获取查询出来的所有数据"""
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def find_count(self,sql):
        """返回查询数据的条件"""
        self.conn.commit()
        return self.cur.execute(sql)

    def close(self):
        """关闭游标，断开连接"""
        self.cur.close()
        self.conn.close()

