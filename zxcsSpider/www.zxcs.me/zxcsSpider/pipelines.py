# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

import pymysql

class ZxcsspiderPipeline():
    def process_item(self, item, spider):
        db = pymysql.connect(host="Localhost或数据库IP",user="Mysql数据库用户名",password="Mysql数据库密码",db="zxcs",charset="utf8")
        cursor = db.cursor()

        cursor.execute('insert into zxcsdb1(bookname,author,bookcode,booksize,bookmes,bookcate1,bookcate2,download1,download2)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (item['bookname'], item['author'], item['bookcode'], item['booksize'], item['bookmes'], item['bookcate1'], item['bookcate2'], item['download1'], item['download2']))


        db.commit()

        cursor.close()
        db.close()

        return item