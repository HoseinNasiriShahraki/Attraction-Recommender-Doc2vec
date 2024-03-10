import scrapy
from get_link import get_link
url_list = get_link()

class ContentfetcherSpider(scrapy.Spider):
    name = "ContentFetcher"
    allowed_domains = ["www.kojaro.com"]
    start_urls = url_list[0]
    
    def start_requests(self): 
        url_list = get_link()     # Enter your target URL here 
        for url in url_list: 
            yield scrapy.Request(url=url, callback=self.parse)
    
    
    def parse(self, response):
        yield {
            'Name': response.xpath('.//*[@id="AttractionSearch"]/div[1]/div/div/div[1]/div[1]/h1/span/text()').get(),
            'Address': response.xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "address", " " ))]/text()').get(),
            'Phone Number': response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "phoneNumberDirecttion", " " ))]/text()').get(),
            'Email': response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "dis-inline", " " )) and contains(concat( " ", @class, " " ), concat( " ", "medium", " " ))]/text()').get(),
            'Web Site': response.xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "text-darken-3", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "font-rem", " " ))]/text()').get(),
            'Rating': response.xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "showRateHotel", " " ))]/text()').get(),
            'Country': response.xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "attraction-heritage", " " ))]//span/text').get(),
            'Body': response.xpath('//sub | //*[(@id = "bodyContainer")]//p/text()').extract() #this returns a list of docs
        }
        