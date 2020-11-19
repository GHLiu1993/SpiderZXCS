# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZxcsspiderItem(scrapy.Item):
    bookname = scrapy.Field()
    author = scrapy.Field()
    bookcode = scrapy.Field()
    booksize = scrapy.Field()
    bookmes = scrapy.Field()
    bookcate1 = scrapy.Field()
    bookcate2 = scrapy.Field()
    Evaluation1 = scrapy.Field()
    Evaluation2 = scrapy.Field()
    Evaluation3 = scrapy.Field()
    Evaluation4 = scrapy.Field()
    Evaluation5 = scrapy.Field()
    download1 = scrapy.Field()
    download2 = scrapy.Field()


    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
