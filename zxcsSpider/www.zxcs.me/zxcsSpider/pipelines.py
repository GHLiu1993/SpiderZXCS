# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from openpyxl import Workbook
class ZxcsspiderPipeline():

    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['bookname', 'author', 'bookcode', 'booksize', 'bookmes', 'bookcate1','bookcate2','download1','download2'])  # 设置表头


    def process_item(self, item, spider):
        line = [item['bookname'], item['author'], item['bookcode'], item['booksize'], item['bookmes'],
                item['bookcate1'], item['bookcate2'], item['download1'],item['download2']]  # 把数据中每一项整理出来
        self.ws.append(line)
        self.wb.save('zxcs.xlsx')
        return item
