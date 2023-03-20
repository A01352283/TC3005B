# Output format: data = {'urls': product_links}
import scrapy

class KavakspiderSpider(scrapy.Spider):
    name = "kavakSpider"
    
    def start_requests(self):
        url = "https://www.kavak.com/mx/seminuevos/?page=0"
        yield scrapy.Request(url, 
                            meta=dict(playwright = True,
                                      playwright_include_page = True,
                                      errback=self.errback,
                                      playwright_page_methods={"click": PageMethod("click", selector="a")}
                            ))
        # To route our requests through 
        #scrapy-playwright we just need to enable it in the Request meta dictionary 
        #by setting meta={'playwright': True}.

    def parse(self, response):
        

        yield scrapy.Request('https://www.kavak.com/mx/usado/jeep-renegade-sport-suv-2017?id=244926'
                             , callback=self.parse_page, meta={'playwright': True})

        """ urls = response.css('a.card::attr(href)').getall()

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_page, meta={'playwright': True}) """


    async def parse_page(self, response):

        # Get the text of a h1 with the class "title"
        # Translate the previous comment to spanish
        carPathSpan = response.css("span.path::text").getall()
        brand = carPathSpan[1]
        model = carPathSpan[2]
        #yearModel = carPathSpan[3]

        # Get the text of a <p> with the class "value" which is inside a <div> with the class 
        # "filter-container" if the other <p> inside the <div> has the text "Año"
        year = response.css('div.filter-container:contains("Año") p.value::text').get()
        
        # Get the price of the car
        price = response.css("span.normal::text").getall()

        # Get the text of a <p> with the class "description" which is inside a <div> with the class 
        # "feature-content" if the other <p> inside the <div> has the text "Transmisión"
        transmission = response.css('div.feature-content:contains("Transmisión") p.description::text').get()

        # Get the text of a <p> with the class "description" which is inside a <div> with the class 
        # "feature-content" if the other <p> inside the <div> has the text "Combustible"
        #combustible = response.css('div.feature-content:contains("Combustible") p.description::text').get()

        # Get the text of a <p> with the class "description" which is inside a <div> with the class 
        # "feature-content" if the other <p> inside the <div> exavtly matches the text "Combustible"
        #litros = response.css('div.feature-content:contains("Combustible") p.description::text').get()
        
        # Get the text of a <p> with the class "description" which is inside a <div> with the class 
        # "feature-content" if the other <p> inside the <div> has the text "Litros"
        litros = response.css('div.feature-content:contains("Litros") p.description::text').get()

        yield {'brand': brand, 'model': model, 'year': year, 
               'price': price, 'transmission': transmission}