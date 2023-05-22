import scrapy
from Spiderlian.items import SpiderlianItem


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["cs.lianjia.com"]
    start_urls = ["https://cs.lianjia.com/zufang/"]

    def parse(self, response):
        name = response.xpath('//div[@class="content__list--item--main"]//p[@class="content__list--item--title"]/a/text()').extract()  # 是去对Selector对象取值
        price = response.xpath('//div[@class="content__list--item--main"]//em/text()').extract()
        link = response.xpath('//div[@class="content__list--item--main"]//a[@class="twoline"]/@href').extract()
        for names, prices, links in zip(name, price, link):
            # 实例化item模板类，键名必须和字段名统一
            item = SpiderlianItem()
            l = response.urljoin(links)
            item['name'] = names.strip()
            item['price'] = prices
            item['link'] = l
            yield item
