import scrapy
from product import Product

# https://www.guenstiger.de/alle-kategorien.html

class GuenstigerSpider(scrapy.Spider):

    name = "guenstiger"

    def start_requests(self):

        urls = [
            'https://www.guenstiger.de/Katalog/Suche/{}.html',
        ]

        keywords = ['laptop', 'toaster']

        for url in urls:
            for keyword in keywords:
                url = url.format(keyword)
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for product in response.css('div.productsListRow'):
            title = str(product.css('div.productDetails::attr(title)').get())#.attrib['title'])
            price = str(product.css('span.PRICEVALUELEFT::text').get()) + str(product.css('span.PRICEVALUERIGHT::text').get()) + "€"

            #print(" price: "+price)
            print(title+" : "+price)
            #print("product_list "+str(product)

        next_page = response.css('div.L3 a').attrib['href']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
