#!/usr/bin/python3 安装mysql.connector驱动

import mysql.connector


class mysqlDB:
    def __init__(self):
        # 打开数据库连接
        self.db = mysql.connector.connect(host='172.16.0.44', port=3306, user='root', passwd='123456', database='grab',
                                          charset='utf8')

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    def insertNews(self, title="", link="", image=""):
        sql = "insert into news (title, link, image) values (%s, %s, %s)"
        value = (title, link, image)
        self.cursor.execute(sql, value)
        self.db.commit()

    def close(self):
        self.db.close