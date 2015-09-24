# -*- coding: utf-8 -*-
__author__ = 'jpradas'
import scrapy
from items import Restaurante
import io


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

class tripSpider(scrapy.Spider):
    name = "Trip"
    allowed_domains = ["tripadvisor.es"]
    rango=drange(1, 2500, 30)
    cad=["http://www.tripadvisor.es/RestaurantSearch-g187529-oa%g-a_Action.PAGE-a_ajax.1-a_availSearchEnabled.true-a_date.2015__2D__09__2D__24-a_itags.10591-a_people.2-a_time.20%%3A00%%3A00-jpopularity-Valencia_Valencia_Province_Valencian_Country.html#EATERY_LIST_CONTENTS" % x for x in rango]

    start_urls =  cad

    def parse(self, response):
        #for sel in response.xpath('//div/[@class="desc_article"]/ul'):
        #for sel in response.xpath('//div[contains(@class,"listing listingIndex")]'):
        item = Restaurante()

        cad=response.xpath('//div[@class="shortSellDetails"]/h3/a/text()').extract()
        link=response.xpath('//div[@class="shortSellDetails"]/h3/a/@href').extract()
        pos=response.xpath('//div[@class="popIndex popIndexDefault"]/text()').extract()
        i=0
        for c in pos:
            item['posicion'] = c[:c.find(" ")].replace("\n", "")
            item['nombre'] = cad[i].replace("\n", "")
            item['link'] = link[i].replace("\n", "")
            i=i+1

            yield item
            #f.write("'" + item['nombre'] + "','"+ item['posicion'] +'\n')





