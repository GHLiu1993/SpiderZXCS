# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import pymysql

class ZxcsspiderPipeline():
    def process_item(self, item, spider):
        db = pymysql.connect(host="数据库IP地址",user="数据库用户名",password="数据库密码",db="zxcs",charset="utf8")
        cursor = db.cursor()

        cursor.execute(
                        'insert into zxcsAllBooks(书名,作者,编号,大小,简介,分类1,分类2,仙草,良草,干草,枯草,毒草,下载链接1,下载链接2)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                   (
                                    item['bookname'], item['author'], item['bookcode'],
                                    item['booksize'], item['bookmes'], item['bookcate1'],
                                    item['bookcate2'], item['Evaluation1'],item['Evaluation2'],
                                    item['Evaluation3'],item['Evaluation4'],item['Evaluation5'],
                                    item['download1'], item['download2']
                                   )
                       )


        db.commit()

        cursor.close()
        db.close()

        return item
