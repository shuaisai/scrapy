import scrapy
from AnimalPro.items import AnimalproItem

class AnimalSpider(scrapy.Spider):
    name = 'animal'
    # allowed_domains = ['www.xx.com']
    start_urls = ['http://pic.netbian.com/4kdongwu/']

    url ='http://pic.netbian.com/4kdongwu/index_%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            src = 'http://pic.netbian.com' + li.xpath('./a/img/@src').extract_first()

            item = AnimalproItem()
            item['src'] = src

            yield item

        if self.page_num <= 20:
            new_url = self.url % self.page_num
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)



