# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BiliPipeline:

    # def close_spider(self, spider):
    #     self.f = open("data.txt", 'a', encoding="utf-8")

    # def open_spider(self, spider):
    #     self.f.close()

    def process_item(self, item, spider):
        f = open("data.txt", 'a', encoding="utf-8")
        f.writelines(str(item["ID"]))
        f.writelines("\n")
        f.writelines(item["title"])
        f.writelines("\n")
        f.writelines(str(item["classification"]))
        f.writelines("\n")
        f.writelines(item["text"])
        f.writelines("\n")
        f.close()
        
        return item
