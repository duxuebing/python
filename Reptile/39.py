import requests

url = 'http://httpbin.org/get'
headers = {
    'User-Agent':'Mozilla/5.0'
}
# 网上找的免费代理ip
proxies = {
    'http':'http://121.13.252.58:41564',
    'https':'https://121.13.252.62:41564'
}
html = requests.get(url,proxies=proxies,headers=headers,timeout=5).text
print(html)