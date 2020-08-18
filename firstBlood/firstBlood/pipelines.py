# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FirstbloodPipeline:

    def open_spider(self, spider):
        print('开始爬虫。。。。。。')
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        age = item['age']
        self.fp.write(author + ':' + '年龄:' + age + content + '\n')

    def close_spider(self, spider):
        print('爬取结束。。。。。。')
        self.fp.close()


