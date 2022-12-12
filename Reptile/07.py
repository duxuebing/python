from urllib import request,parse

# 1.拼url地址
url = 'http://www.baidu.com/s?wd={}'
word = input('请输入搜索内容:')
params = parse.quote(word)
full_url = url.format(params)
print(full_url)

# 2.发请求保存到本地
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'} # 重构请求头
req = request.Request(url=full_url,headers=headers) # 创建请求对应
res = request.urlopen(req) # 获取响应对象
html = res.read().decode('utf-8') # 获取响应内容
# print(html)

# 3.保存文件至当前目录
# 把爬取的照片保存至本地，此处需要使用 Python 编程的文件 IO 操作
filename = word + '.html'
with open(filename,'w',encoding='utf-8') as f:
    f.write(html)