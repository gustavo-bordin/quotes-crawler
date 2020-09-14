import scrapy
from database import Database


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ["https://www.pensador.com/frases/"]

    database = Database()

    def parse(self, response):
        quotes = []
        cards = response.xpath("//*[@class='thought-card']")
        for card in cards:
            content = card.xpath(
                ".//p[@class='frase fr']/text()").extract_first()
            author = card.xpath(
                ".//span[@class='autor']/a/text()").extract_first()

            quotes.append({"content": content, "author": author})

        self.database.insert(quotes)

        pagination_buttons = response.xpath("//a[@class='nav']")
        switch_page = pagination_buttons[-1]

        if "Próxima" in switch_page.xpath('text()').extract_first():
            next_page_url = switch_page.xpath('@href').extract_first()
            absolute_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_url)
