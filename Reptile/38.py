import requests
url = 'https://img0.baidu.com/it/u=3434652324,1525281230&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=500'

# 简单定义浏览器ua信息
headers = {'User-Agent':'Mozilla/4.0'}

# ​#读取图片需要使用content属性
html = requests.get(url=url,headers=headers).content

#以二进制的方式下载图片
with open('/Users/apple/Desktop/python_logo.jpg','wb') as f:
    f.write(html)