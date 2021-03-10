# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Bili1Pipeline:
    def process_item(self, item, spider):
        f = open("other.txt", 'a', encoding="utf-8")
        f.writelines(str(item["ID"]))
        f.writelines(" ")
        f.writelines(str(item["view"]))
        f.writelines(" ")
        f.writelines(str(item["favor"]))
        f.writelines(" ")
        f.writelines(str(item["like"]))
        f.writelines(" ")
        f.writelines(str(item["reply"]))
        f.writelines(" ")
        f.writelines(str(item["share"]))
        f.writelines(" ")
        f.writelines(str(item["coin"]))      
        f.writelines(" ")
        f.writelines(str(item["dislike"]))
        f.writelines("\n")
        f.close()
        return item
