# -*-coding:utf-8-*-
import pymysql

#创建对象
db = pymysql.connect(host='localhost',user='root',password='12345678',database='maoyandb')
cursor = db.cursor()

# sql语句执性，单行插入
info_list = ['刺杀,小说家','雷佳音,杨幂','2021-2-12']
sql = 'insert into filmtab values(%s,%s,%s)'

#列表传参
cursor.execute(sql,info_list)
db.commit()

# 关闭
cursor.close()
db.close()