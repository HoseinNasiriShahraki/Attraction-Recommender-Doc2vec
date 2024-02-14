import scrapy
from get_link import get_link
url_list = get_link()

class ContentfetcherSpider(scrapy.Spider):
    name = "ContentFetcher"
    allowed_domains = ["www.kojaro.com"]
    start_urls = url_list[0]
    
    def parse(self, response):
        yield {
            'URL': response.xpath('.//a/@href').get(),
            'Quote': response.xpath('.//p/text()').get(),
        }
        
