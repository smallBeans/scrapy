import scrapy
from lxml import etree
from firstscrapy.items import CountryItem

class CountrySpider(scrapy.Spider):
    name = 'country'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    def parse(self, response):
        domain = "http://example.webscraping.com"
        tree = etree.HTML(response.text)
        print("start handle html***************************")
        country_list = tree.xpath('//section[@id="main"]//div[@id="results"]//td/div/a')
        # print(etree.tostring(country_list).decode("utf-8"))
        for node in country_list:
            item = CountryItem()
            hrefUrl = node.xpath('./self::*/@href')[0]
            # print("链接：" + hrefUrl)
            item['countryUrl'] = domain + hrefUrl
            imgUrl = node.xpath('./self::*/img/@src')[0]
            # print("图片：" + imgUrl)
            item['countryIcon'] = domain + imgUrl
            text = node.xpath('./self::*/text()')[0]
            item['countryName'] = text
            # print("文本：" + text)
            yield item
        print("end handle html***************************")