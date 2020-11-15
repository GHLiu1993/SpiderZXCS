# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

class ZxcsspiderPipeline():



    def __init__(self):
            self.f = open("zxcs.json","w")
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii = False)+"/n"
        self.f.write(content)
        return item
    def close_spider(self,spider):
        self.f.close()
