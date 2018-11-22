
import scrapy

class Spider(scrapy.Spider):
    name = 'spider'
    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/' ,'http://quotes.toscrape.com/page/1/']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        pass


