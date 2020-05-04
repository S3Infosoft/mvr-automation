# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MvrSpider(scrapy.Spider):
    name = 'mvr'
    allowed_domains = ['www.booking.com']
    start_urls = ['http://www.booking.com/']





    def parse(self, response):
        # print(response.text)
        self.log('I just visited: ' + response.url)
        item = {}
        item['prop_type'] = []

        for i in range(4):
            print(i)
            item['prop_type'].extend(response.css('#basiclayout > div.d-index__section.bui-spacer--largest.js-ds-layout-events-bh_promotions > div > ul > li:nth-child('+str(i+1)+') > div > div.bui-card__content > h3 > a::text').extract())

        # print(response.css('#basiclayout > div.d-index__section.bui-spacer--largest.js-ds-layout-events-bh_promotions > div > ul > li:nth-child(1) > div > div.bui-card__content > h3 > a::text').extract())
        yield item
        # view(response)  #this is command line tool to open the webpage of response

        # filename = response.url.split("/")[-1] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # / html / body / div[6] / div / div[1] / div[2] / div[12] / div / ul / li[1] / div / div[2] / h3 / a