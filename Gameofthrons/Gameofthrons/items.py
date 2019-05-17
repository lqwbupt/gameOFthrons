# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


import scrapy

class UrlItem(scrapy.Item):
        # define the fields for your item here like:
        # name = scrapy.Field()
        url = scrapy.Field()

class GameofthronsItem(scrapy.Item):
        # define the fields for your item here like:
        # name = scrapy.Field()
        chapter = scrapy.Field()  # 章节
        content = scrapy.Field()  # 小说内容
        characters = scrapy.Field()  # 文中出现的角色
        url = scrapy.Field()  # 章节网址，方便返工