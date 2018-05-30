import scrapy

class AmazonbooksSpider(scrapy.Spider):
    name = "AmazonbooksSpider"

    def start_requests(self):
        url = 'https://www.amazon.fr/gp/bestsellers/books/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'author': response.xpath('//span[@class="a-size-small a-color-base"]//text()').extract_first(),
            'title': response.xpath('//div[@class="p13n-sc-truncate p13n-sc-line-clamp-1"]//text()').extract_first().strip()
        }
#        for item in response.css('div.zg_itemWrapper'):
#            yield {
#                'title': item.css('div.p13n-sc-truncate.p13n-sc-line-clamp-1::text').extract_first().strip(),
#                'author': item.css('a.a-size-small.a-link-child::text').extract_first() 
#                    if item.css('a.a-size-small.a-link-child') 
#                    else item.css('span.a-size-small.a-color-base::text').extract_first() 
#            }
 
