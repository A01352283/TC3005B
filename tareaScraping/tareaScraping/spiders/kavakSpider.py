import scrapy
from scrapy_playwright.page import PageMethod

# scrapy crawl kavakSpider -s JOBDIR=crawls/kavakcrawl  

class KavakspiderSpider(scrapy.Spider):
    name = "kavakSpider"

    # To disable headless mode
    """ custom_settings = {
        "PLAYWRIGHT_BROWSER_TYPE": "chromium",
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": False,
        },
        "PLAYWRIGHT_CONTEXT_OPTIONS": {
            "ignoreHTTPSErrors": True,
            "viewport": {
                "width": 1920,
                "height": 1080,
            },
        }
    } """
    
    def start_requests(self):
        for i in range(0, 381):
            url = "https://www.kavak.com/mx/seminuevos/?page=" + str(i)
            yield scrapy.Request(url, callback=self.parse, meta={"playwright": True})
            
        """ url = "https://www.kavak.com/mx/seminuevos/?page=0"
        yield scrapy.Request(url, callback=self.parse, meta={"playwright": True}) """  
    
    # Get the urls of each car page from the preview cards
    def parse(self, response):

        # Get the urls until there are 30 urls
        urls = response.css('a.card::attr(href)').getall()

        # Visit each car page
        for url in urls:
            yield scrapy.Request(url, 
                                callback=self.parse_page, 
                                meta={"playwright": True,
                                    "playwright_page_methods": [PageMethod("click", "h3.accordion-label")]
                                    }
                                )
        # To route our requests through scrapy-playwright we just need to enable it in the Request meta dictionary 
        # by setting meta={'playwright' True}.


    # Scrape the data from each car page
    async def parse_page(self, response):
        # Get the text of a h1 with the class "title"
        carPathSpan = response.css("span.path::text").getall()
        marca = carPathSpan[1]
        modelo = carPathSpan[2]

        # Get the text of a <p> with the class "value" which is inside a <div> with the class "filter-container" if the 
        # other <p> inside the <div> has the text "Año"
        año = response.css('div.filter-container:contains("Año") p.value::text').get()
        
        # Get the precio of the car
        precio = response.css("span.normal::text").getall()

        # Get the text of a <p> with the class "description" which is inside a <div> with the class "feature-content" if
        # the other <p> inside the <div> has the text "Transmisión"
        transmisión = response.css('div.feature-content:contains("Transmisión") p.description::text').get()
        
        # Get the text of a <p> with the class "description" which is inside a <div> with the class "feature-content" if
        # the other <p> inside the <div> has the text "Combustible"
        divsCombustible = response.css('div.feature-content:contains("Combustible") p.description::text').getall()
        rendimiento = divsCombustible[0] 
        combustible = ""
        try:
            combustible = divsCombustible[1]
        except:
            combustible = None       
        
        # Get the text of a <p> with the class "description" which is inside a <div> with the class "feature-content" if
        # the other <p> inside the <div> has the text "Litros"
        litros = response.css('div.feature-content:contains("Litros") p.description::text').get()

        #tipo_vehiculo = response.css('div.feature-content:contains("Tipo de Carrocería") p.description::text').get()


        yield {'marca': marca, 'modelo': modelo, 'año': año, 
                'precio': precio, 'transmisión': transmisión, 'rendimiento': rendimiento,
                'combustible': combustible, 'litros': litros}

    async def errback_close_page(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()