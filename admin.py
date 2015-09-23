__author__ = 'jpradas'


import scrapy
from spiders.trip_Spider import tripSpider

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import settings

process = CrawlerProcess(get_project_settings())

process.crawl(tripSpider)

process.start()

