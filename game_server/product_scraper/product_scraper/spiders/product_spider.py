import scrapy

class ProductSpider(scrapy.Spider):

    name = "products"

     def __init__(self, *args, **kwargs):
        # args from our django view.
        self.url = kwargs.get('url')
        self.domain = kwargs.get('domain')
        self.start_urls = [self.url]
        self.allowed_domains = [self.domain]

        ProductSpider.rules = [
           Rule(LinkExtractor(unique=True), callback='parse_item'),
        ]
        super(ProductSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        # You can tweak each crawled page here
        # Don't forget to return an object.
        i = {}
        i['url'] = response.url
        return i
