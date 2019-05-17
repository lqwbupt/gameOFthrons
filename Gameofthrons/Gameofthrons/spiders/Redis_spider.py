# -*- coding: utf-8 -*-
# @Author: Liu
# @Date  : 2019-05-10 21:46:27


import scrapy
from lxml import etree
from scrapy.http import Request
from Gameofthrons.items import UrlItem



class Spider(scrapy.Spider):
    name = 'Redis_spider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'Gameofthrons.pipelines.RedisPipeline': 300
        }}
    main_url = 'http://www.sbkk88.com'
    bas_url = 'http://www.sbkk88.com/mingzhu/waiguowenxuemingzhu/bingyuhuozhige'
    tail_url = '.html'

    def start_requests(self):
        for i in range(1, 6):
            url = self.bas_url + 'b' + str(i) + '/'
            yield Request(url, self.parse)
        # http://www.sbkk88.com/mingzhu/waiguowenxuemingzhu/bingyuhuozhige

    def parse(self, response):
        selector = etree.HTML(response.text)
        son_urls = selector.xpath(
            '//div[@class="mingzhuMain"]/div[@class="mingzhuLeft"]/ul[@class="leftList"]/li/a/@href')
        # item = UrlItem()
        for son_url in son_urls:
            item = UrlItem()
            son_url = self.main_url + son_url
            item['url'] = son_url
            yield item


