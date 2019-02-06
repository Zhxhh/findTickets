from scrapy import cmdline
import sys

argv = sys.argv[1]
if argv == '-n':
	cmdline.execute('scrapy crawl findTickets_spider'.split())
if argv == '-o':
	cmdline.execute('scrapy crawl findTickets_spider -o result.csv'.split())
