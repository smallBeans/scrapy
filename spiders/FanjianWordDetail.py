import scrapy
from lxml import etree
from firstscrapy.items import FanJianWordDetailItem
import json

class FanjianDetailSpiderV1(scrapy.Spider):
    name = 'fanJianWordDetail'
    allowed_domains = ['www.fanjian.net']
    start_urls = ['http://www.fanjian.net/jbk/anli.html']

    # 爬取地址
    url_list = []
    # """"""
    data = []
    with open('fanjianword.json',"r",encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    f.close()
    # print(data)
    for i in data:
        url_list.append(i['wordUrl'])
    print(url_list)
    start_urls = url_list

    def parse(self, response):
        tree = etree.HTML(response.text)
        print("start handle html***************************")
        titleHtml = tree.xpath('//h1[@class="view-word-title"]/text()')[0]
        item = FanJianWordDetailItem()
        item['wordName'] = titleHtml
        # detailHtmlNode = tree.xpath('//div[@class="view-main"]/p')[0]
        # detailHtml = detailHtmlNode.xpath('./self::*/text()')[0]
        subDetailHtmlNode = tree.xpath('//div[@class="view-main"]')[0]
        listSubDetailHtmlNode = subDetailHtmlNode.xpath('./self::*/*')
        list = []
        for node in listSubDetailHtmlNode:
            print(node.tag)
            nodeType = node.tag
            if nodeType == "p" or nodeType == "h2":
                pText = etree.tostring(node.xpath('./self::*')[0],encoding='utf-8').decode('utf-8')
                list.append(pText)
            else:
                continue
        item['subList'] = list
        yield item
        print("end handle html***************************")