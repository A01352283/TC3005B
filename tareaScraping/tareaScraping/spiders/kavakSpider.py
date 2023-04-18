import scrapy
import json


class KavakspiderSpider(scrapy.Spider):
    name = "kavakSpider"
    allowed_domains = ["www.kavak.com"]
    start_urls = ["https://www.kavak.com/mx/seminuevos"]
        
    def parse(self, response):
        # Extract links to product pages
        # Extract the link from the <a> tag with class "card"
        product_links = response.css('a.card::attr(href)').getall()

        data = {'urls': product_links}
        
        yield data
        
        # Follow each product link and parse the product page
        """ for product_link in product_links:
            yield response.follow(product_link, callback=self.parse_product) """

    """ def parse_product(self, response):
        # Extract data from the product page
        data = {}
        data['title'] = response.css('.product-title::text').get()
        data['price'] = response.css('.product-price::text').get()
        data['litres'] = response.css('.feature:contains("Litres") + .feature-value::text').get()
        data['transmission'] = response.css('.feature:contains("Transmission") + .feature-value::text').get()

        yield data """
