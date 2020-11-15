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
    # Evaluation = scrapy.Field()
    download1 = scrapy.Field()
    download2 = scrapy.Field()


