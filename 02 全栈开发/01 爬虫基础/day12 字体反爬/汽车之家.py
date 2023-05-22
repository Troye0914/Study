import re
import os
import json
import requests
from bs4 import BeautifulSoup
from jsonpath import jsonpath
from font_map import GetFontMap


class Autohome(object):
    def __init__(self):
        self.url = 'https://koubeiipv6.app.autohome.com.cn/pc/series/list'
        self.url_detail = {}
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        self.index_page = 1
        self.index_comment = 1
        self.params = {
            'pm': 3,
            'seriesId': 5499,
            'pageIndex': self.index_page,
            'pageSize': 20,
            'yearid': 0,
            'ge': 0,
            'seriesSummaryKey': 0,
            'order': 0
        }
        # 用json存储数据
        self.autohome_data = {}

    def get_data(self):
        for i in range(1, 11):
            print('开始爬取第{}页 -->'.format(i))
            data_index = requests.get(self.url, headers=self.headers, params=self.params).json()
            show_id = jsonpath(data_index, '$..list[0:20].showId')
            self.index_comment = 1
            all_comment = {}
            for id in show_id:
                print('正在爬取第{}条评论..'.format(self.index_comment))
                url_detail = 'https://k.autohome.com.cn/detail/view_{}.html#pvareaid=2112108'.format(id)
                data = requests.get(url_detail, headers=self.headers).text
                trans_data = self.trans_data(data)
                comment = self.parse_data(trans_data)
                all_comment['第{}条'.format(self.index_comment)] = comment
                self.autohome_data['第{}页'.format(self.index_page)] = all_comment
                self.save_data()
                self.index_comment += 1
            print('')
            self.autohome_data['第{}页'.format(self.index_page)] = all_comment
            self.save_data()
            self.index_page += 1

    def trans_data(self, html_data):
        url_font = re.findall("format\('embedded-opentype'\).*?url\('(.*?)'\)\sformat\('woff'\);", html_data, re.S)[0]
        if not os.path.exists('./font_ttf'):
            os.mkdir('./font_ttf')
        file_path = './font_ttf/' + url_font.split('/')[-1]
        response = requests.get(url_font, headers=self.headers)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        font_map = GetFontMap(file_path).font_map()
        for k, v in font_map.items():
            html_data = html_data.replace(k, v)
        return html_data

    def parse_data(self, html_data):
        soup = BeautifulSoup(html_data, 'lxml')
        items = soup.select('.kb-con .kb-item')
        comment = {}
        for item in items:
            content = list(item.stripped_strings)
            if content[0] == '最满意' or content[0] == '最不满意':
                comment[content[0]] = ''.join(content[1:])
            else:
                comment['{}({}分)'.format(content[0], content[1])] = ''.join(content[2:])
        return comment

    def save_data(self):
        with open('autohome_data.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.autohome_data, ensure_ascii=False))

    def run(self):
        self.get_data()
        self.save_data()


if __name__ == '__main__':
    autohome = Autohome()
    autohome.run()
