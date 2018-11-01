# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CountryItem(scrapy.Item):
    countryName = scrapy.Field()
    countryIcon = scrapy.Field()
    countryUrl = scrapy.Field()

class FanJianWordItem(scrapy.Item):
    wordName = scrapy.Field()
    wordUrl = scrapy.Field()

class FanJianWordDetailItem(scrapy.Item):
    wordName = scrapy.Field()
    wordDetail = scrapy.Field()
    subList = scrapy.Field()

class FanJianWordSubDetailItem(scrapy.Item):
    key = scrapy.Field()
    value = scrapy.Field()