import scrapy

class MytheresaSpider(scrapy.Spider):
    name='mytheresa'
    start_urls=['https://www.mytheresa.com/int_en/men/shoes.html']
    
    def parse(self,response):
        for products in response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[7]/ul'):
            yield {'link':products.xpath('li/a[1]/@href').getall()}