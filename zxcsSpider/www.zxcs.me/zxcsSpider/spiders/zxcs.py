import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from..items import ZxcsspiderItem
import re

class ZxcsSpider(CrawlSpider):

    name = 'zxcs'
    allowed_domains = ['zxcs.me']
    start_urls = ['http://www.zxcs.me/sort/23']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.zxcs.me/download.php?id=\d+'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'http://www.zxcs.me/post/\d+'), callback='parse_item',follow = False),
        Rule(LinkExtractor(allow=r'http://www.zxcs.me/sort/\d+'), follow=False),
    )

    def parse_item(self, response):
        item = ZxcsspiderItem()

        Alist = response.xpath("//body/div[@class='wrap']/div[@id='pleft']")

        for bookmessage in Alist:
            re1 = re.compile(r'《(.*)》')
            re2 = re.compile(r'作者：(.*)')
            re3 = re.compile(r'id=(.*)')
            re4 = re.compile(r'【内容简介】：(.*)')
            url3 = bookmessage.xpath("./div[@id='content']/div/div/p/a/@href").extract_first()

            namelists = bookmessage.xpath("./div[@id='content']/h1/text()").extract_first()
            namelists2 = re.findall(re1,namelists )
            item['bookname'] = namelists2[0]

            authorlist = bookmessage.xpath("./div[@id='content']/h1/text()").extract_first()
            authorlist2 = re.findall(re2,authorlist )
            item['author'] = authorlist2[0]

            codelist = bookmessage.xpath("./div[@id='content']/div/div/p/a/@href").extract_first()
            codelist2 = re.findall(re3,codelist)
            item['bookcode'] = codelist2[0]

            mes = bookmessage.xpath("./div[@id='content']/p[3]/text()").extract()

            uecd = " ".join([i.replace("\n","",) for i in mes])
            uecd2 = uecd.replace(u'\xa0', u'')
            bookmeslist = uecd2.replace(u'\u3000', u'')
            bookmeslist2 = re.findall(re4,bookmeslist)
            item['bookmes'] = bookmeslist2[0]
            item['bookcate1'] = bookmessage.xpath("./div[@id='ptop']/a[2]/text()").extract_first()
            item['bookcate2'] = bookmessage.xpath("./div[@id='ptop']/a[3]/text()").extract_first()

            url3s = response.urljoin(url3)
            yield scrapy.Request(url=url3s,
                                 callback = self.parse_two_html,
                                 meta={'item': item},
                                 )
    def parse_two_html(self,response):
        Blist = response.xpath("//body/div/div[@class='content']")
        item = response.meta['item']
        for bookmessage2 in Blist:
            item['download1'] = bookmessage2.xpath("./div[@class='panel'][1]/div[@class='panel-body']/span[1]/a/@href").extract_first()
            item['download2'] = bookmessage2.xpath("./div[@class='panel'][1]/div[@class='panel-body']/span[2]/a/@href").extract_first()
            booksize_list = bookmessage2.xpath("./div[1]/div[1]/ul/li[3]/text()").extract_first()
            booksizelist = re.compile(r'小说大小 ：(.*)').findall(booksize_list)
            item['booksize'] = booksizelist[0]

        yield item


