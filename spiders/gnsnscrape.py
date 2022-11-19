import scrapy
class gnsnspi(scrapy.Spider):
    name = "gnsnspi"
    start_urls = ["https://genshin.honeyhunterworld.com/db/char/characters/?lang=EN"]
    def parse(self, response):
        chars = response.css("div.char_sea_cont a")
        for char in [a.attrib["href"] for a in chars]:
            char_url = response.urljoin(char)
            yield scrapy.Request(char_url, callback = self.parse_characters)
    def parse_characters(self, response):
        name = response.css("div.custom_title::text").get()
        serifu_block = response.css("table.item_main_table")
        serifu = serifu_block.css("td::text").getall()
        yield{
            "name": name,
            "lines": serifu
        }