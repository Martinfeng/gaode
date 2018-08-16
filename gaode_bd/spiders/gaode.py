#coding:utf8
import scrapy
import urllib
import json
from gaode_bd.items import GaodeBdItem

class Boundary(scrapy.Spider):
    name = "tj_gaode"
    def start_requests(self):
        url_main = "https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20" \
                   "&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000" \
                   "&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=17&city=120000&keywords="
        xiaoqu_list=open("tj_xiaoqu.csv",'r').read().split('\n')
        for xiaoqu in xiaoqu_list:
            url=url_main+urllib.quote(xiaoqu)
            yield scrapy.Request(url=url,callback=self.parse,meta={"xiaoqu":xiaoqu.decode('utf8'),"count":0})

    def parse(self, response):
        data=json.loads(response.text)

        count=response.meta['count']
        while data['status']=='6' and count<5:
            count+=1
            yield scrapy.Request(url=response.url,callback=self.parse
                                 ,dont_filter=True,meta={"xiaoqu":response.meta['xiaoqu'],"count":count})
        item=GaodeBdItem()
        item['xiaoqu']=response.meta['xiaoqu']
        try:
            item['boundary']=data['data']['poi_list'][0]['domain_list'][-1][u'value']
        except:
            item['boundary']=''
        item['link']=response.url

        yield item