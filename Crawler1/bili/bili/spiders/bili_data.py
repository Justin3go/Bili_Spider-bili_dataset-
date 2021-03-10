import scrapy
from bili.items import BiliItem


class BiliDataSpider(scrapy.Spider):
    name = 'bili_data'
    # allowed_domains = ['www.bilibili.com']
    start_urls = ["https://www.bilibili.com/read/cv1049193"]
    url = "https://www.bilibili.com/read/cv%d"
    cv_number = 1049193
    
    def parse(self, response):
        if(response.status == 200):
            
            title = response.xpath('//h1[@class="title"]/text()').extract()
            text = response.xpath('//div[@class="article-holder"]//p/text()').extract()
            classification = response.xpath('//a[@class="category-link"]//span/text()').extract()
            # 创建item对象，将解析到的数据存储到items对象中
            item = BiliItem()
            item["ID"] = self.cv_number
            item["title"] = title
            item["text"] = text
            item["classification"] = classification
            yield item

        if self.cv_number <= 101000000:
            print("爬取到第%d页数据\n" % self.cv_number)
            self.cv_number += 1
            try:
                new_url = format(self.url % self.cv_number)
                print("更新---------------url:%s\n" % new_url)
                yield scrapy.Request(url=new_url, callback=self.parse, dont_filter=True)
            except Exception:
                print("ohohohohohohoh!")
                self.cv_number += 1
                new_url = format(self.url % self.cv_number)
                yield scrapy.Request(url=new_url, callback=self.parse)
