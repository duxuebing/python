#导入模块
from hashlib import md5

#待加密的url
url="https://www.dydytt.net/html/gndy/dyzz/list_23_2.html"

# 生成MD5对象
secret = md5()

# 加密url
secret.update(url.encode())

# 提取十六进制的加密串
finger = secret.hexdigest()
print(finger)