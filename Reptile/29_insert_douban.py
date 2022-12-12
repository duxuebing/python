#coding:utf-8
from urllib import request
import re
import time
import random
import csv
import ssl
from ua_info import ua_list
import pymysql

# 定义一个爬虫类
class MaoyanSpider(object):
    # 初始化
    # 定义初始页面url
    def __init__(self):
        self.url = 'https://book.douban.com/top250?start={}'
        # 数据库连接对象
        self.db = pymysql.connect(host='localhost',user='root',password='12345678',database='maoyandb')
        # 创建游标对象
        self.cursor = self.db.cursor()

    # 请求函数
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        ssl._create_default_https_context = ssl._create_unverified_context
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)

    # 解析函数
    def parse_html(self, html):
        # 正则表达式
        re_bds = '<td.*?title="(.*?)".*?pl">(.*?)</p.*?td>'
        # 生成正则表达式对象
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)

    # 保存数据函数，使用python内置csv模块
    def save_html(self, r_list):
        L = []
        sql = 'insert into douban values(%s,%s)'
        for r in r_list:
            t = (
                r[0].strip(),
                r[1].strip()
            )
            L.append(t)
            print(L)
        try:
            self.cursor.executemany(sql,L)
            self.db.commit()
        except:
            self.db.rollback()

        # 生成文件对象
        # with open('douban.csv', 'a', newline='', encoding="utf-8") as f:
        #     # 生成csv操作对象
        #     writer = csv.writer(f)
        #     # 整理数据
        #     for r in r_list:
        #         name = r[0].strip()
        #         star = r[1].strip()
        #         L = [name, star]
        #         # 写入csv文件
        #         writer.writerow(L)

    # 主函数
    def run(self):
        # 抓取第一页数据
        for offset in range(0, 10, 25):
            url = self.url.format(offset)
            print(url)
            self.get_html(url)
            # 生成1-2之间的浮点数
            time.sleep(random.uniform(1, 2))

# 以脚本方式启动
if __name__ == '__main__':
    # 捕捉异常错误
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print("错误:", e)