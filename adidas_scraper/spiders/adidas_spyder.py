import scrapy
from scrapy_splash import SplashRequest
import re
class AdidasSpider(scrapy.Spider):
    name = 'adidas'
    start_urls = ['https://shop.adidas.jp/men/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        category_links = response.css('a.lpc-miniTeaserCard_link::attr(href)').getall()
        new_category_links = []
        for link in category_links:
            for i in range(1, 8):
                new_link = link + f"&page={i}"
                new_category_links.append(new_link)

        for link in new_category_links:
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
        product_price = response.css('.articlePrice .price-value::text').get()
        category_name =  response.css('.groupName .categoryName::text').get()
        available_sizes = response.css(
            'ul.sizeSelectorList li.sizeSelectorListItem button.sizeSelectorListItemButton::text').getall()

        sense_of_the_size = response.css('div.label.test-label span::text').getall()
        image_url = response.css('div.article_image_wrapper div.article_image img::attr(src)').extract()
        title_of_description = response.css('h2.itemName::text').get()
        general_description = response.css('div.description_part.details .commentItem-mainText::text').get()
        general_description_itemization = response.css('ul.articleFeatures li.test-feature::text').getall()
        tag_list = response.css('div.test-category_link.null.css-vxqsdw a::text').getall()

        # Extracting rating information
        identifier_pattern = r'"identifier":"(\d+)"'
        review_body_pattern = r'"reviewBody":"(.*?)"'
        date_published_pattern = r'"datePublished":"(.*?)"'
        rating_value_pattern = r'"ratingValue":"(.*?)"'
        identifiers = re.findall(identifier_pattern, response.text)
        review_bodies = re.findall(review_body_pattern, response.text)
        dates_published = re.findall(date_published_pattern, response.text)
        rating_values = re.findall(rating_value_pattern, response.text)
        reviews = []

        for identifier, review_body, date_published, rating_value in zip(identifiers, review_bodies, dates_published,
                                                                         rating_values):
            review = {
                "identifier": identifier,
                "review_body": review_body,
                "date_published": date_published,
                "rating_value": rating_value
            }
            reviews.append(review)





        yield {
            'product_name': product_name,
            'product_url': product_url,
            'product_price': product_price,
            'category_name': category_name,
            'available_sizes': available_sizes,
            'sense_of_the_size': sense_of_the_size,
            'image_url': image_url,
            'title_of_description': title_of_description,
            'general_description': general_description,
            'general_description_itemization': general_description_itemization,
            'kws':tag_list,
            'reviews':reviews

            # Add more fields as needed
        }
