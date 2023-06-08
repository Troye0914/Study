# https://www.bbc.co.uk/news/world
import random
import time

import requests
import Proxies
from lxml import etree


class BBC():
    def __init__(self):
        self.url = 'https://www.bbc.co.uk/search?q=climate&d=news_gnl'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'referer': 'https://www.bbc.co.uk/search?q=&d=news_gnl'
        }
        self.proxies = Proxies.proxies

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        http_doc = response.text
        return http_doc

    def parse_data(self):
        # http_doc = self.get_data(self.url)
        http_doc = open('demo.html', 'r', encoding='utf-8').read()
        xml_doc = etree.HTML(http_doc)
        titles = xml_doc.xpath('//ul[@role="list" and @spacing="responsive"]/li//span[@aria-hidden="false"]')
        links = xml_doc.xpath('//ul[@role="list" and @spacing="responsive"]/li//a/@href')
        for title, link in zip(titles, links):
            time.sleep(random.randint(2, 5))
            sub_html_doc = self.get_data(link)
            sub_xml_doc = etree.HTML(sub_html_doc)
            article = sub_xml_doc.xpath('//article')
            print(len(article))

    def run(self):
        self.parse_data()


if __name__ == '__main__':
    bbc = BBC()
    bbc.run()
