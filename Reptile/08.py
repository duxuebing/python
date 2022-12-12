# Python 函数式编程可以让程序的思路更加清晰、易懂。接下来，使用函数编程的思想更改上面代码。
# 定义相应的函数，通过调用函数来执行爬虫程序。修改后的代码如下所示：
from urllib import request
from urllib import parse
# 拼接URL地址
def get_url(word):
  url = 'http://www.baidu.com/s?{}'
  #此处使用urlencode()进行编码
  params = parse.urlencode({'wd':word})
  url = url.format(params)
  # print(url)
  return url

# 发请求,保存本地文件
def request_url(url,filename):
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
  # 请求对象 + 响应对象 + 提取内容
  req = request.Request(url=url,headers=headers)
  res = request.urlopen(req)
  html = res.read().decode('utf-8')
  # 保存文件至本地
  with open(filename,'w',encoding='utf-8') as f:
    f.write(html)

# 主程序入口
if __name__ == '__main__':
  word = input('请输入搜索内容:')
  url = get_url(word)
  filename = word + '.html'
  request_url(url,filename)