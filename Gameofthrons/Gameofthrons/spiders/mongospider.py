# -*- coding: utf-8 -*-
# @Author: Liu
# @Date  : 2019-05-10 20:05:27




from lxml import etree
from Gameofthrons.items import GameofthronsItem
from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    name = 'mongospider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'Gameofthrons.pipelines.GotspiderPipeline': 300
        }}
    redis_key = 'myspider:start_urls'  # 从redis里面读url

    def __init__(self):
        self.characterlists = []
        with open(r'../roles.txt', 'r',encoding='UTF-8') as f:
            lines = f.readlines()
        for line in lines:
            self.characterlists.append((line.strip()).split('\t'))

    def parse(self, response):
        item = GameofthronsItem()
        item['url'] = response.url
        selector = etree.HTML(response.text)
        item['chapter'] = selector.xpath('//div[@id="f_title1"]/h1/text()')[0]
        content = ''.join(list(map(lambda p: p.strip(), selector.xpath(
            '//div[@id="f_content1"]/div[@id="f_article"]/p/text()'))))
        item['content'] = content
        characters = []
        for row in self.characterlists:
            for role in row:
                if role in content:
                    characters.append(row[0])
        item['characters'] = '/'.join(list(set(characters)))
        yield item


# def get_content(self, response):
#     item = GotspiderItem()
#     item['url']'http://quotes.toscrapy.com/page/1/', = str(response.meta['son_url'])
#     selector = etree.HTML(response.text)
#     item['chapter'] = selector.xpath('//div[@id="f_title1"]/h1/text()')[0]
#     content = ''.join(list(map(lambda p: p.strip(), selector.xpath(
#         '//div[@id="f_content1"]/div[@id="f_article"]/p/text()'))))
#     item['content'] = content
#     characters = []
#     for row in self.characterlists:
#         for role in row:
#             if role in content:
#                 characters.append(row[0])
#     item['characters'] = '/'.join(list(set(characters)))
#     yield item

