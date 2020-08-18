import scrapy


class TaobaospiderSpider(scrapy.Spider):
    name = 'taobaospider'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.taobao.com/']

    def parse(self, response):
        pass



