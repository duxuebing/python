import csv
from urllib import request,parse
import ssl
import re

# 1.拼url地址
title = 'douban'
url = 'https://book.douban.com/top250?start=0'
# print(url)

# 2.发请求保存到本地
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
ssl._create_default_https_context = ssl._create_unverified_context
req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')
# print(html)

re_bds = '<td.*?title="(.*?)".*?pl">(.*?)</p.*?td>'
pattern = re.compile(re_bds,re.S)
r_list = pattern.findall(html)

# 3.保存文件至当前目录
# filename = title + '.csv'
with open('douban.csv','a',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    for r in  r_list:
        name = r[0].strip()
        print(name)
        star = r[1].strip()
        print(star)
        L = [name, star]
        writer.writerow(L)
        print(name, star)