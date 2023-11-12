import scrapy

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    start_urls = ['http://category.dangdang.com/cp01.54.06.00.00.00.html']

    def parse(self, response):
        books = response.xpath('//ul[@class="bigimg"]/li')
        for book in books:
            title = book.xpath('p[@class="name"]/a/text()').get()
            author = book.xpath('p[@class="search_book_author"]/span[1]/a/text()').get()
            price = book.xpath('p[@class="price"]/span/text()').get()
            yield {
                'title': title,
                'author': author,
                'price': price
            }
