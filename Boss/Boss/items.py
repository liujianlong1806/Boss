# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zhiwei = scrapy.Field()
    gongzi = scrapy.Field()
    gongsi = scrapy.Field()
    didian = scrapy.Field()
    jingyan  = scrapy.Field()
    xueli = scrapy.Field()
