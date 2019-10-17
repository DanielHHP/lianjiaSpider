# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DealItem

LABEL_MAPPING = {
    '链家编号': 'lianjia_id',
    '挂牌时间': 'listing_time',
    '房屋年限': 'last_transaction_duration',
    '挂牌价格（万）': 'listed_price',
    '成交周期（天）': 'transaction_duration',
    '调价（次）': 'price_change_count',
    '带看（次）': 'visit_count',
    '关注（人）': 'follower_count',
    '浏览（次）': 'page_view_count',

    '房屋户型': 'house_type',
    '建筑面积': 'area',
    '房屋朝向': 'orientation',
    '建成年代': 'build_year',
    '所在楼层': 'floor',
    '建筑类型': 'building_type',
}

class LianjiaDealSpider(scrapy.Spider):
    name = 'lianjiadealspider'
    deal_url = 'https://bj.lianjia.com/chengjiao/'
    page_limit = 0

    def start_requests(self):
        start_community_id = getattr(self, 'communityid', None)
        self.page_limit = int(getattr(self, 'pagelimit', 0))
        if start_community_id is None:
            self.logger.error('start community id not defined')
            return
        start_url = self.deal_url + '/%s/' % (start_community_id)
         
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        for info in response.css('div.info'):
            # 详情页
            yield scrapy.Request(url=info.css('div.title a').attrib['href'], callback=self.parse_detail)

        page_attrib = response.css('div.house-lst-page-box').attrib
        page_data = json.loads(page_attrib['page-data'])
        total_page = page_data['totalPage']
        cur_page = page_data['curPage']
        page_url = page_attrib['page-url']
        next_page = cur_page + 1
        if self.page_limit > 0 and cur_page > self.page_limit:
            self.logger.info('Navigate to limit page %s stop', self.page_limit)
        elif next_page <= total_page:
            self.logger.info('Navigate to page num %s', next_page)
            page_url = page_url.replace('{page}', str(next_page))
            yield response.follow(page_url, callback=self.parse)
        else:
            self.logger.info('Navigate to final page %s stop', total_page)
    
    def label_to_item(self, label_pair, deal_item):
        if label_pair[0] in LABEL_MAPPING:
            deal_item[LABEL_MAPPING[label_pair[0]]] = label_pair[1].strip()

    def parse_detail(self, response):
        deal_item = DealItem()
        # 标题区域
        deal_item['title'] = response.css('div.house-title div.wrapper').css('::text').get('')
        deal_item['deal_date'] = response.css('div.house-title div.wrapper span::text').get('').split(' ')[0].strip()
        deal_item['community'] = deal_item['title'].split()[0].strip()

        # 基本属性
        for basic_info_label in response.css('div.base div.content ul li'):
            self.label_to_item(basic_info_label.css('::text').getall(), deal_item)

        # 交易属性
        for traction_info_label in response.css('div.transaction div.content ul li'):
            self.label_to_item(traction_info_label.css('::text').getall(), deal_item)

        # 总体信息
        deal_item['transaction_price'] = response.css('span.dealTotalPrice i::text').get()
        deal_item['history_trade_count'] = str(len(response.css('ul.record_list li')))
        for msg_info_label in response.css('div.msg span'):
            self.label_to_item(list(reversed(msg_info_label.css('::text').getall())), deal_item)

        yield deal_item