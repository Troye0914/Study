import re
import csv
import requests
from jsonpath import jsonpath


class IndexSpider(object):
    def __init__(self):
        self.url = "https://data.weibo.com/index/ajax/newindex/getchartdata"
        self.payload = {
            'wid': '1091323832915',
            'dateGroup': '1hour'
        }
        self.wid_url = "https://data.weibo.com/index/ajax/newindex/searchword"
        self.wid_payload = {'word': '端午节'}
        self.headers = {
            'referer': 'https://data.weibo.com/index/newindex?visit_type=trend&wid=1091323832915',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.f = open('微指数.csv', 'w', encoding='utf-8')
        self.csv_w = csv.writer(self.f)
        self.csv_w.writerow(['检索目标', '时间', '指数'])

    def get_data(self):
        response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
        return response.json()

    def parse_data(self, data):
        index_times = jsonpath(data, '$..x')[0]
        indexs = jsonpath(data, '$..s')[0]
        for index_time, index in zip(index_times, indexs):
            self.csv_w.writerow([self.wid_payload['word'], index_time, index])

    def get_wid_data(self):
        response = requests.request("POST", self.wid_url, headers=self.headers, data=self.wid_payload)
        json_data = response.text
        wid = re.findall(r'<li\swid=\\"(.*?)\\"\sword=.*?', json_data, re.S)
        return wid[0]

    def run(self):
        index_times = ['1hour', '1day', '1month', '3month']
        name = input('请输入您要检索的关键字：')
        self.wid_payload['word'] = name
        wid = self.get_wid_data()
        self.payload['wid'] = wid
        for i in index_times:
            self.payload['dateGroup'] = i
            data = self.get_data()
            self.parse_data(data)


if __name__ == '__main__':
    wb = IndexSpider()
    wb.run()
