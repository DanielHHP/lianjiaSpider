# -*- coding: utf-8 -*-
import scrapy
import re
import time
from ..items import DealItem

class LianjiaDealSpider(scrapy.Spider):
    name = 'lianjiadealspider'
    deal_url = 'https://bj.lianjia.com/chengjiao/'

    def start_requests(self):
        start_url = self.deal_url + '/c1111027376953/'
         
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        for info in response.css('div.info'):
            dealItem = DealItem()
            dealItem['title'] = info.css('.title a::text').get().strip()
            dealItem['title'] = info.css('.title a::text').get().strip()
            dealItem['title'] = info.css('.title a::text').get().strip()
            dealItem['title'] = info.css('.title a::text').get().strip()
            dealItem['title'] = info.css('.title a::text').get().strip()
            dealItem['title'] = info.css('.title a::text').get().strip()
            dealItem['title'] = info.css('.title a::text').get().strip()
            dealItem['title'] = info.css('.title a::text').get().strip()
            dealItem['title'] = info.css('.title a::text').get().strip()

            yield dealItem
        pageInfo = response.css("div.house-lst-page-box")
        

    def detail_url(self,response):
        'http://bj.lianjia.com/ershoufang/dongcheng/pg2/'
        for i in range(1,101):
            url = 'http://bj.lianjia.com/ershoufang/{}/pg{}/'.format(response.meta["id2"],str(1))
            time.sleep(2)
            try:
                contents = requests.get(url)
                contents = etree.HTML(contents.content.decode('utf-8'))
                houselist = contents.xpath('/html/body/div[4]/div[1]/ul/li')
                for house in houselist:
                    try:
                        item = DealItem()
                        item['title'] = house.xpath('div[1]/div[1]/a/text()').pop()
                        item['community'] = house.xpath('div[1]/div[2]/div/a/text()').pop()
                        item['model'] = house.xpath('div[1]/div[2]/div/text()').pop().split('|')[1]
                        item['area'] = house.xpath('div[1]/div[2]/div/text()').pop().split('|')[2]
                        item['focus_num'] = house.xpath('div[1]/div[4]/text()').pop().split('/')[0]
                        item['watch_num'] = house.xpath('div[1]/div[4]/text()').pop().split('/')[1]
                        item['time'] = house.xpath('div[1]/div[4]/text()').pop().split('/')[2]
                        item['price'] = house.xpath('div[1]/div[6]/div[1]/span/text()').pop()
                        item['average_price'] = house.xpath('div[1]/div[6]/div[2]/span/text()').pop()
                        item['link'] = house.xpath('div[1]/div[1]/a/@href').pop()
                        item['city'] = response.meta["id1"]
                        self.url_detail = house.xpath('div[1]/div[1]/a/@href').pop()
                        #item['Latitude'] = self.get_latitude(self.url_detail)
                    except Exception:
                        pass
                    yield item
            except Exception:
                pass