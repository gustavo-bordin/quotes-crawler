import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ["https://www.pensador.com/frases/"]

    quotes = []

    def parse(self, response):

        cards = response.xpath("//*[@class='thought-card']")
        for card in cards:
            content = card.xpath(
                ".//p[@class='frase fr']/text()").extract_first()
            author = card.xpath(
                ".//span[@class='autor']/a/text()").extract_first()

            self.quotes.append({"content": content, "author": author})

        pagination_buttons = response.xpath("//a[@class='nav']")
        switch_page = pagination_buttons[-1]

        if "Próxima" in switch_page.xpath('text()').extract_first():
            next_page_url = switch_page.xpath('@href').extract_first()
            absolute_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_url)

        else:
            print(self.quotes)
