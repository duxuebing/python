import json
ditc_info={"name" : "c语言中文网","PV" : "50万","UV" : "20万","create_time" : "2010年"}
with open("web.josn","a") as f:
    json.dump(ditc_info,f,ensure_ascii=False)