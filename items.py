# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Restaurante(scrapy.Item):
    nombre = scrapy.Field()
    posicion = scrapy.Field()
    link = scrapy.Field()

class RdpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
