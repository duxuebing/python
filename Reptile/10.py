#---------------这是自己根据前面所学改写的---------------#
from urllib import request,parse
import ssl

# 拼接URL地址
def get_url(word):
  url = 'https://tieba.baidu.com/f/search/res?isnew=1&kw=&qw={}'
  # word = input('请输入搜索内容:')
  params = parse.quote(word)
  full_url = url.format(params)
  url_2 = full_url + '&rn=10&un=&only_thread=0&sm=1&sd=&ed=&pn=2'
  # print(url_2)
  return url_2

# 发请求,保存本地文件
def request_url(url_2,filename):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}  # 重构请求头
  ssl._create_default_https_context = ssl._create_unverified_context
  req = request.Request(url=url_2, headers=headers)  # 创建请求对应
  res = request.urlopen(req)  # 获取响应对象
  html = res.read().decode("GBK", "ignore")  # 获取响应内容
  # print(html)
  # 保存文件至本地
  with open(filename, 'w', encoding='GBK') as f:
      f.write(html)

# 主程序入口
if __name__ == '__main__':
  word = input('请输入搜索内容:')
  url = get_url(word)
  filename = word + '.html'
  request_url(url,filename)