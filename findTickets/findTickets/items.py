# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindticketsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	trainNo = scrapy.Field()
	arrStationName = scrapy.Field()
	dptStationName = scrapy.Field()
	dptTime = scrapy.Field()
	arrTime = scrapy.Field()
	interval = scrapy.Field()
	seats = scrapy.Field()
	dptDate = scrapy.Field()
