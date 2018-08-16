# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class GaodeBdPipeline(object):
    def process_item(self, item, spider):
        with open("tj_xiaoqu_bd.txt","a") as outfile:
            outfile.write('|'.join([x.encode('gbk') for x in item.values()])+'\n')
        return item
