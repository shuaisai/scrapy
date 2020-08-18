import scrapy
from firstBlood.items import FirstbloodItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):

        div_list = response.xpath('//div[@id="content"]/div/div[2]/div')

        content_list = []
        for div in div_list:
            autor = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = ''.join(div.xpath('./a[1]/div/span//text()').extract())
            age = div.xpath('./div[1]/div/text()')[0].extract()

            item = FirstbloodItem()
            item['author'] = autor
            item['content'] = content
            item['age'] = age

            yield item





