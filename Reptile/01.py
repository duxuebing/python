#导包,发起请求使用urllib库的request请求模块
import urllib.request
# urlopen()向URL发请求,返回响应对象,注意url必须完整
response=urllib.request.urlopen('http://www.baidu.com/')
# print(response)

html = response.read().decode('utf-8')#提取响应内容
print(html)#打印响应内容

# bytes = response.read() # read()返回结果为 bytes 数据类型
# print(bytes)
# string = response.read().decode() # decode()将字节串转换为 string 类型
# print(string)
# url = response.geturl() # 返回响应对象的URL地址
# print(url)
# code = response.getcode() # 返回请求时的HTTP响应码
# print(code)