import scrapy
from bili1.items import Bili1Item
import json


class OtherDataSpider(scrapy.Spider):
    name = 'other_data'
    # allowed_domains = ['bilibili.com']
    start_urls = ['https://api.bilibili.com/x/article/viewinfo?id=1047645&jsonp=jsonp']
    url_other = "https://api.bilibili.com/x/article/viewinfo?id=%d&jsonp=jsonp"
    cv_number = 1047645

    def parse(self, response):
        if(response.status == 200):
            j = json.loads(response.body)
            item = Bili1Item()
            item["ID"] = self.cv_number
            try:
                item["view"] = j['data']['stats']['view']
                item["favor"] = j['data']['stats']['favorite']
                item["like"] = j['data']['stats']['like']
                item["reply"] = j['data']['stats']['reply']
                item["share"] = j['data']['stats']['share']
                item["coin"] = j['data']['stats']['coin']
                item["dislike"] = j['data']['stats']['dislike']
            except Exception:
                item["view"] = '$'
                item["favor"] = '$'
                item["like"] = '$'
                item["reply"] = '$'
                item["share"] = '$'
                item["coin"] = '$'
                item["dislike"] = '$'
            yield item

        if self.cv_number <= 101000000:
            print("爬取到第%d页数据\n" % self.cv_number)
            self.cv_number += 1
            try:
                new_url_other = format(self.url_other % self.cv_number)
                print("更新---------------url:%s\n" % new_url_other)
                yield scrapy.Request(url=new_url_other, callback=self.parse, dont_filter=True)
            except Exception:
                print("ohohohohohohoh!")
                self.cv_number += 1
                new_url_other = format(self.url_other % self.cv_number)
                yield scrapy.Request(url=new_url_other, callback=self.parse)
