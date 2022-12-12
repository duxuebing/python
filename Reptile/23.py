# coding=gbk
from urllib import request
import re
import time
import random
from ua_info import ua_list
import pymysql

class MaoyanSpider(object):
    def __init__(self):
        #初始化属性对象
        self.url = 'https://maoyan.com/board/4?offset={}'
        #数据库连接对象
        self.db = pymysql.connect(
            'localhost','root','123456','maoyandb',charset='utf8')
        #创建游标对象
        self.cursor = self.db.cursor()
    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接解析
        self.parse_html(html)
    def parse_html(self,html):
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)
    def save_html(self, r_list):
        L = []
        sql = 'insert into movieinfo values(%s,%s,%s)'
        # 整理数据
        for r in r_list:
            t = (
                r[0].strip(),
                r[1].strip()[3:],
                r[2].strip()[5:15]
            )
            L.append(t)
            print(L)
        # 一次性插入多条数据 L:[(),(),()]
        try:
            self.cursor.executemany(sql,L)
            # 将数据提交数据库
            self.db.commit()
        except:
            # 发生错误则回滚
            self.db.rollback()
    def run(self):
        for offset in range(0,11,10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.uniform(1,3))
        # 断开游标与数据库连接
        self.cursor.close()
        self.db.close()
if __name__ == '__main__':
    start=time.time()
    spider = MaoyanSpider()
    spider.run()
    end=time.time()
    print("执行时间:%.2f" % (end-start))