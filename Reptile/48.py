import json
item_list = []
item = {'website': 'C语言中文网', 'url': "c.biancheng.net"}
for k,v in item.items():
    item_list.append(v)
with open('info_web.json', 'a') as f:
    json.dump(item_list, f, ensure_ascii=False)