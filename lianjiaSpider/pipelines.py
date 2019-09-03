# -*- coding: utf-8 -*-
import csv
import logging
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LianjiaspiderPipeline(object):
    # community -> {lianjiaid -> data}
    cache_dict = {}

    def open_spider(self, spider):
        self.logger = logging.getLogger(__name__)

    def close_spider(self, spider):
        sample_item = None
        for community in self.cache_dict:
            file_cache = {}
            file_name = '%s.csv' % (community)
            if os.path.isfile(file_name):
                with open(file_name, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        file_cache[row['lianjia_id']] = row
            
            for lianjia_id, item in self.cache_dict[community].items():
                file_cache[lianjia_id] = item
                sample_item = item
            
            if sample_item is not None:
                with open(file_name, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=sample_item.keys())
                    writer.writeheader()
                    for lianjia_id, item in file_cache.items():
                        writer.writerow(item)

    def process_item(self, item, spider):
        community = item.get('community')
        if not community:
            self.logger.warning('%s has no community info. Will not store data', item)
            return item
        community_cache = self.cache_dict.setdefault(community, {})
        community_cache[item.get('lianjia_id')] = dict(item)

        return item
