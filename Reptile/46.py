# coding:utf8
import json
#JOSN字符串
website_info='{"name" : "c语言中文网","PV" : "50万","UV" : "20万","create_time" : "2010年"}'
print(website_info,type(website_info))
py_dict=json.loads(website_info)
print("python字典数据格式：%s；数据类型：%s"% (py_dict,type(py_dict)))

# 注意：上述示例中 JSON 字符串看上去和 Python 字典非常相似，但是其本质不同，JOSN 是字符串类型，而 Python 字典是 dict 类型。