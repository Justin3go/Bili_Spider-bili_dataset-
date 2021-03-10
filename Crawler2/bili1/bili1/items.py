# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Bili1Item(scrapy.Item):
    # define the fields for your item here like:
    ID = scrapy.Field()
    view = scrapy.Field()
    favor = scrapy.Field()
    like = scrapy.Field()
    reply = scrapy.Field()
    share = scrapy.Field()
    coin = scrapy.Field()
    dislike = scrapy.Field()
