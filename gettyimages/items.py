# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item

class GettyimagesItem(scrapy.Item):
    # define the fields for your item here like:
    #file_urls = scrapy.Field()
    pass

class ImgData(Item):
    file_urls=scrapy.Field()
    images=scrapy.Field()