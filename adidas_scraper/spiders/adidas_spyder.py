import scrapy
from scrapy_splash import SplashRequest

class AdidasSpider(scrapy.Spider):
    name = 'adidas'
    start_urls = ['https://shop.adidas.jp/men/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        # Extract category links
        category_links = response.css('a.lpc-miniTeaserCard_link::attr(href)').getall()
        for link in category_links:
            yield SplashRequest(response.urljoin(link), self.parse_category, args={'wait': 2})

    def parse_category(self, response):
        # Extract product links
        product_links = response.css('div.articleDisplayCard-children a::attr(href)').getall()
        for product_link in product_links:
            yield SplashRequest(response.urljoin(product_link), self.parse_product, args={'wait': 2})

    def parse_product(self, response):
        # Extract product details and store them
        product_name = response.css('h1::text').get()
        product_url = response.url
        product_price = response.css('.js-price::text').get()
        # Extract other details like rating, comments, etc.
        # Store the data (you can use a database or a spreadsheet library)
        yield {
            'product_name': product_name,
            'product_url': product_url,
            'product_price': product_price,
            # Add more fields as needed
        }
