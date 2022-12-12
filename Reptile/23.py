# coding=gbk
from urllib import request
import re
import time
import random
from ua_info import ua_list
import pymysql

class MaoyanSpider(object):
    def __init__(self):
        #��ʼ�����Զ���
        self.url = 'https://maoyan.com/board/4?offset={}'
        #���ݿ����Ӷ���
        self.db = pymysql.connect(
            'localhost','root','123456','maoyandb',charset='utf8')
        #�����α����
        self.cursor = self.db.cursor()
    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # ֱ�ӽ���
        self.parse_html(html)
    def parse_html(self,html):
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)
    def save_html(self, r_list):
        L = []
        sql = 'insert into movieinfo values(%s,%s,%s)'
        # ��������
        for r in r_list:
            t = (
                r[0].strip(),
                r[1].strip()[3:],
                r[2].strip()[5:15]
            )
            L.append(t)
            print(L)
        # һ���Բ���������� L:[(),(),()]
        try:
            self.cursor.executemany(sql,L)
            # �������ύ���ݿ�
            self.db.commit()
        except:
            # ����������ع�
            self.db.rollback()
    def run(self):
        for offset in range(0,11,10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.uniform(1,3))
        # �Ͽ��α������ݿ�����
        self.cursor.close()
        self.db.close()
if __name__ == '__main__':
    start=time.time()
    spider = MaoyanSpider()
    spider.run()
    end=time.time()
    print("ִ��ʱ��:%.2f" % (end-start))