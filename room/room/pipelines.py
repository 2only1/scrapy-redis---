# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo

class MongoPipeline:
    def open_spider(self,spider):
        # 链接mongoDB
        self.client = pymongo.MongoClient()
        # 获取集合
        self.lianjia = self.client.room.lianjia
    def process_item(self, item, spider):
        # 数据存入mongoDB
        self.lianjia.insert_one(item)
        return item
    def close_spider(self,spider):
        # 关闭mongoDB
        self.client.close()