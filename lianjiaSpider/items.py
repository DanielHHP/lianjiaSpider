# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DealItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 交易信息
    # 链家编号
    lianjia_id = scrapy.Field()
    # 成交信息日期
    deal_date = scrapy.Field()
    # 挂牌时间
    listing_time = scrapy.Field()
    # 房屋年限，满五
    last_transaction_duration = scrapy.Field()
    # 历史成交次数
    history_trade_count = scrapy.Field()
    # 挂牌价格（万）
    listed_price = scrapy.Field()
    # 成交价格（万）
    transaction_price = scrapy.Field()
    # 成交周期（天）
    transaction_duration = scrapy.Field()
    # 调价次数
    price_change_count = scrapy.Field()

    # 浏览信息
    # 带看次数
    visit_count = scrapy.Field()
    # 关注（人）
    follower_count = scrapy.Field()
    # 浏览（次）
    page_view_count = scrapy.Field()

    # 基础属性
    # 标题
    title = scrapy.Field()
    # 小区
    community = scrapy.Field()
    # 户型
    house_type = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 朝向
    orientation = scrapy.Field()
    # 建成年代
    build_year = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 建筑类型
    building_type = scrapy.Field()
    