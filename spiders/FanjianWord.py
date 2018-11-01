import scrapy
from lxml import etree
from firstscrapy.items import FanJianWordItem

class FanjianSpider(scrapy.Spider):
    name = 'fanJianWord'
    allowed_domains = ['www.fanjian.net']
    start_urls = ['http://www.fanjian.net/jbk']

    def parse(self, response):
        # domain = "http://www.fanjian.net/jbk"
        tree = etree.HTML(response.text)
        print("start handle html***************************")
        word_list = tree.xpath('//ul[@class="word-list"]/li/dl/dd/a')
        for node in word_list:
            item = FanJianWordItem()
            hrefUrl = node.xpath('./self::*/@href')[0]
            item['wordUrl'] = hrefUrl
            wordName = node.xpath('./self::*/text()')[0]
            item['wordName'] = wordName
            yield item
        print("end handle html***************************")