import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exporters import JsonLinesItemExporter
from scrapy.utils.reactor import install_reactor

install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")


class PropertySpider(scrapy.Spider):
    name = "properties"
    
    start_url_template = "https://www.sreality.cz/hledani/prodej/byty?strana={page_number}"
    start_page = 1
    end_page = 25

    custom_settings = {
        'FEEDS': {'output.json': {'format': 'jsonlines'}},  # Output in JSON Lines format
    }

    def start_requests(self):
        for page_number in range(self.start_page, self.end_page + 1):
            yield scrapy.Request(url=self.start_url_template.format(page_number=page_number), callback=self.parse)

    def parse(self, response):
        # Parse items on the current page
        for property_item in response.css('div.property'):
            yield {
                'title': property_item.css('span.name::text').get().strip(),
                'href': property_item.css('a::attr(href)').get(),
                'image_url': property_item.css('img::attr(src)').get(),
            }


# Run the spider
process = CrawlerProcess(settings={
    "TWISTED_REACTOR": 'asyncio'
})
process.crawl(PropertySpider)
process.start()
