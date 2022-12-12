from urllib import request,parse
import time
import random
import ssl
from ua_info import ua_list #使用自定义的ua池

#定义一个爬虫类
class TiebaSpider(object):
    #初始化url属性
    def __init__(self):
        self.url='https://tieba.baidu.com/f/search/res?isnew=1&kw=&{}'
    # 1.请求函数，得到页面，传统三步
    def get_html(self,url):
        ssl._create_default_https_context = ssl._create_unverified_context
        req=request.Request(url=url,headers={'User-Agent':random.choice(ua_list)})
        res=request.urlopen(req)
        #windows会存在乱码问题，需要使用 gbk解码，并使用ignore忽略不能处理的字节
        #linux不会存在上述问题，可以直接使用decode('utf-8')解码
        html=res.read().decode("GBK", "ignore")
        return html
    # 2.解析函数，此处代码暂时省略，还没介绍解析模块
    def parse_html(self):
        pass
    # 3.保存文件函数
    def save_html(self,filename,html):
        with open(filename, 'w', encoding='GBK') as f:
            f.write(html)
    # 4.入口函数
    def run(self):
        name=input('输入贴吧名：')
        begin=int(input('输入起始页：'))
        stop=int(input('输入终止页：'))
        # +1 操作保证能够取到整数
        for page in range(begin,stop+1):
            pn=(page-1)*1
            params={
                'qw':name,
                'rn':'10',
                'un':'',
                'only_thread':'0',
                'sm':'1',
                'sd':'',
                'ed':'',
                'pn':str(pn)
            }
            #拼接URL地址
            params=parse.urlencode(params)
            # print(params)
            url=self.url.format(params)
            # print(url)
            #发请求
            html=self.get_html(url)
            #定义路径
            filename='{}-{}页.html'.format(name,page)
            self.save_html(filename,html)
            #提示
            print('第%d页抓取成功'%page)
            #每爬取一个页面随机休眠1-2秒钟的时间
            time.sleep(random.randint(1,2))

#以脚本的形式启动爬虫
if __name__=='__main__':
    start=time.time()
    spider=TiebaSpider() #实例化一个对象spider
    spider.run() #调用入口函数
    end=time.time()
    #查看程序执行时间
    print('执行时间:%.2f'%(end-start))  #爬虫执行时间