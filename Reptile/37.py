import requests
response = requests.get('http://www.baidu.com')
print(response.encoding)
response.encoding="utf-8"    #更改为utf-8编码
print(response.status_code)  # 打印状态码
print(response.url)          # 打印请求url
print(response.headers)      # 打印头信息
print(response.cookies)      # 打印cookie信息
print(response.text)  #以字符串形式打印网页源码
print(response.content) #以字节流形式打印