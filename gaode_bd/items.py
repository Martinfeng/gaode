# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GaodeBdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    xiaoqu=scrapy.Field()
    boundary=scrapy.Field()
    link=scrapy.Field()
    pass
