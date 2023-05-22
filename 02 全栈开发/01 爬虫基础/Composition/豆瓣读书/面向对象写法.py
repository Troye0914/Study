"""
豆瓣读书
https://book.douban.com/latest?icn=index-latestbook-all
"""
import json
import os.path
import re
import time
import Proxies
import requests
from lxml import etree
from fake_useragent import UserAgent


class DouBan(object):
    def __init__(self):
        self.url = 'https://book.douban.com/latest'
        self.headers = {
            'user-agent': UserAgent().random
        }
        self.params = {
            'subcat': '全部',
            'p': '1'
        }
        self.proxies = Proxies.proxies
        self.page = 0
        self.num = 0
        self.dict_all_page_data = {}

    def run(self):
        self.get_data()

    def get_data(self):
        if os.path.exists('./douban.json'):
            os.remove('./douban.json')
        for page in range(1, 16):
            self.page = page
            print('正在爬取第{}页-->'.format(self.page))
            self.params['p'] = str(self.page)
            response = requests.get(self.url, headers=self.headers, params=self.params, proxies=self.proxies)
            html_doc = response.text
            self.parse_data_xpath(html_doc)
            # self.parse_data_bs(html_doc)
            time.sleep(2)
        print('爬取完成！')

    """XPath"""
    def parse_data_xpath(self, html_doc):
        xml_doc = etree.HTML(html_doc)
        links = xml_doc.xpath('//a[@class="fleft"]/@href')
        titles = xml_doc.xpath('//div[@class="media__body"]/h2/a')
        details = xml_doc.xpath('p[@class="subject-abstract color-gray"]')
        grades = xml_doc.xpath('//div[@class="media__body"]//span[@class="font-small color-red fleft"]')
        prices = xml_doc.xpath('//div[@class="media__body"]//span[@class="buy-info"]/a')
        self.num = 0
        dict_all_data = {}
        for link, title, detail, grade, price in zip(links, titles, details, grades, prices):
            self.num += 1
            title = title.text
            detail = detail.text.strip()
            grade = '无' if grade.text is None else grade.text
            price = price.text.strip()[4:]
            response = requests.get(link, headers=self.headers)
            html_doc = response.text
            xml_doc = etree.HTML(html_doc)
            content_p = xml_doc.xpath('//div[@id="link-report"]/span[@class="short"]/div[@class="intro"]/p')
            content = ''
            for p in content_p:
                if p.text is not None:
                    content += (p.text + '\n')
            author_p = xml_doc.xpath('//div[@class="indent "]//div[@class="intro"]/p')
            author = ''
            for p in author_p:
                if p.text is not None:
                    author += (p.text + '\n')
            self.save_data_json(dict_all_data, title, detail, grade, price, content, author)

    # """BeautifulSoup"""
    # def parse_data_bs(self, html_doc):
    #     soup = BeautifulSoup(html_doc, 'lxml')
    #     links = soup.find_all('a', {'class': 'fleft'})
    #     titles = soup.find_all('a', {'class': 'fleft'})
    #     details = soup.find_all('p', {'class': 'subject-abstract color-gray'})
    #     grades
    #     prices
    #     for title in titles:
    #         title = title.string


    """正则表达式"""
    def parse_data_re(self, html_doc):
        re.findall('')

    """json存储"""
    def save_data_json(self, dict_all_data, title, detail, grade, price, content, author):
        dict_data = {
            '书名': title,
            '详情': detail,
            '评分': grade,
            '价格': price,
            '内容简介': content,
            '作者简介': author
        }
        dict_all_data.update({f'book{self.num}': dict_data})
        self.dict_all_page_data.update({f'page{self.page}': dict_all_data})
        json_data = json.dumps(self.dict_all_page_data, ensure_ascii=False)
        with open('./douban.json', 'w', encoding='utf-8') as f:
            f.write(json_data)


if __name__ == '__main__':
    douban = DouBan()
    douban.run()
