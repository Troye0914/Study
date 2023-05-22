import scrapy
from doubanspider.items import DoubanspiderItem


class DbSpiderSpider(scrapy.Spider):
    name = "db_spider"
    allowed_domains = ["book.douban.com"]
    start_urls = ["https://book.douban.com/latest?icn=index-latestbook-all"]

    def parse(self, response):
        names = response.xpath('//h2[@class="clearfix"]/a/text()').extract()
        contents = response.xpath('//p[@class="subject-abstract color-gray"]/text()').extract()
        links = response.xpath('//h2[@class="clearfix"]/a/@href').extract()
        for name, content, link in zip(names, contents, links):
            item = DoubanspiderItem()
            item['name'] = name
            item['content'] = content.strip()
            item['link'] = link
            yield scrapy.Request(url=item['link'], callback=self.parse_detail, meta={'item': item})
        part_next = response.xpath('//span[@class="next"]//a/@href').extract_first()
        next_url = response.urljoin(part_next)
        yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        detail = response.xpath('//span[@class="all hidden"]//div[@class="intro"]//p/text()').extract()
        item = response.meta['item']
        item['detail'] = ''.join(detail)
        yield item
