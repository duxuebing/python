# -*-coding:utf-8-*-
import pymysql

#创建对象
db = pymysql.connect(host='localhost',user='root',password='12345678',database='maoyandb')
cursor = db.cursor()

# sql语句执性，列表元组
info_list = [('我不是药神','徐峥','2018-07-05'),('你好,李焕英','贾玲','2021-02-12')]
sql = 'insert into filmtab values(%s,%s,%s)'
cursor.executemany(sql,info_list)
db.commit()

# 关闭
cursor.close()
db.close()