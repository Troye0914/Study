import re
import sys
import time
import random
import requests
from openpyxl import workbook
from bs4 import BeautifulSoup


class Crawler():
    tunnel = "a130.kdltps.com:15818"
    username = "t16908862605129"
    password = "zxcv6789"

    def __init__(self, url):
        self.url = url
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'Accept-Encoding': 'gzip',
            'Referer': url + f'pg100/'
        }
        self.proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": Crawler.username, "pwd": Crawler.password, "proxy": Crawler.tunnel},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": Crawler.username, "pwd": Crawler.password, "proxy": Crawler.tunnel}
        }
        self.wb = workbook.Workbook()
        self.ws = self.wb.active

    def start(self):
        self.ws.append(['标题', '标题链接', '价格', '详情'])
        for i in range(1, 101):
            self.parse_data(i)
            print(f'第{i}页')

    def get_data(self, i):
        try:
            self.url += f'pg{i}/#contentList'
            response = requests.get(self.url, headers=self.headers, proxies=self.proxies).text
            time.sleep(random.uniform(1, 1.5))
            return response
        except:
            sys.setrecursionlimit(10)
            self.get_data(i)

    def parse_data(self, i):
        html_data = self.get_data(i)
        soup = BeautifulSoup(html_data, 'lxml')
        headlines = soup.find_all('p', {'class': 'content__list--item--title'})
        prices = soup.find_all('span', {'class': 'content__list--item-price'})
        details = soup.find_all('p', {'class': 'content__list--item--des'})
        for headline, price, detail in zip(headlines, prices, details):
            # 标题
            h = headline.get_text().strip()
            # 标题的链接
            hl = 'https://cs.lianjia.com' + headline.a['href']
            # 价格
            p = price.get_text()
            # 详情
            d = detail.get_text()
            de = re.sub('/|\n', '', d).replace('    ', '')
            self.save_data(h, hl, p, de)

    def save_data(self, headline, link, price, detail):
        row = [headline, link, price, detail]
        self.ws.append(row)
        self.wb.save('链家.xlsx')


if __name__ == '__main__':
    url = 'https://cs.lianjia.com/zufang/'
    web = Crawler(url)
    web.start()
