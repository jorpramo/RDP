# -*- coding: utf-8 -*-
__author__ = 'jpradas'
import scrapy
from items import Restaurante

class tripSpider(scrapy.Spider):
    name = "Trip"
    allowed_domains = ["tripadvisor.es"]
    start_urls =  ['http://www.tripadvisor.es/Restaurants-g187529-Valencia_Valencia_Province_Valencian_Country.html']

    def parse(self, response):
        #for sel in response.xpath('//div/[@class="desc_article"]/ul'):
        for sel in response.xpath('//div[@class="shortSellDetails"]'):
            item = Restaurante()
            item['nombre'] = sel.xpath('//a/text()').extract()
            item['posicion'] = sel.xpath('//div[@class="popIndex popIndexDefault"]')
            print(item)
            yield item


