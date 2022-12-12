# 解码是对编码后的 URL 进行还原的一种操作，示例代码如下：
# from urllib import parse
# string = '%E7%88%AC%E8%99%AB'
# result = parse.unquote(string)
# print(result)

# 介绍三种拼接 URL 地址的方法。除了使用 format() 函数外，还可以使用字符串相加，以及字符串占位符，总结如下：
# 1、字符串相加
baseurl = 'http://www.baidu.com/s?'
params='wd=%E7%88%AC%E8%99%AB'
url_1 = baseurl + params
print(url_1)

# 2、字符串格式化（占位符）
params='wd=%E7%88%AC%E8%99%AB'
url_2 = 'http://www.baidu.com/s?%s'% params
print(url_2)

# 3、format()方法
url = 'http://www.baidu.com/s?{}'
params='wd=%E7%88%AC%E8%99%AB'
url_3 = url.format(params)
print(url_3)