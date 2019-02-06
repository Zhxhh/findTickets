# -*- coding: utf-8 -*-
import scrapy
import json
import re
import datetime

from findTickets.items import FindticketsItem

class findTicketsSpider(scrapy.Spider):
	name = 'findTickets_spider'
	allowed_domains = ['train.qunar.com']
	count = 3

	def start_requests(self):
		dptDate = '2019-02-06'
		dptPlace = '广州'
		arrPlace = '香港'
		url = 'https://train.qunar.com/dict/open/s2s.do?callback=jQuery172024327106112394636_1549359178749&dptStation=%s&arrStation=%s&date=%s&type=normal&user=neibu&source=site&start=1&num=500&sort=1&_=1549359179005' % (dptPlace,arrPlace,dptDate)
		yield scrapy.Request(url=url,callback=self.parse,meta={'count':1})

	def parse(self,response):
		datas = response.body
		datas = datas.replace(b"/**/jQuery172024327106112394636_1549359178749(",b"")
		datas = datas.replace(b");",b"")
		datas = json.loads(datas)
		datas = datas['data']
		item = FindticketsItem()
		if datas:
				item['dptDate'] = datas['dptDate']
				for data in datas['s2sBeanList']:
					item['trainNo'] = data['trainNo']
					item['arrStationName'] = data['arrStationName']
					item['dptStationName'] = data['dptStationName']
					item['dptTime'] = data['dptTime']
					item['arrTime'] = data['arrTime']
					item['interval'] = data['extraBeanMap']['interval']
					item['seats'] = data['seats']
					yield item
				if(response.meta['count']<self.count):
					dptDate = re.search(r'date=(\d+)-(\d+)-(\d+)',response.url)
					dptDate = datetime.datetime(int(dptDate.group(1)),int(dptDate.group(2)),int(dptDate.group(3)))
					nextDate = dptDate + datetime.timedelta(1)
					nextDate = nextDate.strftime('%Y-%m-%d')
					nextUrl = re.sub(r'date=\d+\-\d+\-\d+', 'date=' + str(nextDate), response.url)
					count = response.meta['count'] + 1
					yield scrapy.Request(url=nextUrl,meta={'count':count})
