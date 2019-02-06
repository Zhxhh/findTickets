# findTickets
Use python crawlers(scrapy framework) to capture ticket/train/bus ticket price information on major travel sites

·目前已实现去哪儿网站火车票抓取

·正常运行程序：
·cd findTickets/findTickets/spiders
·python main.py -n   

#运行并导出信息到result.csv
·python main.py -o  


·可以更改出发地/目的地/出发日期；获取在制定出发日期后的制定时间段内车票信息
·cd findTickets/findTickets/spiders/findTickets_spider.py
#例子
·dptDate = '2019-02-06'
·dptPlace = '广州'
·arrPlace = '香港'
·count = 3   #获取dptDate开始，三天内的车票信息

TODO：
·实现携程/飞猪信息抓取
