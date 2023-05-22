import requests
from jsonpath import jsonpath
from openpyxl import workbook
import sys

wb = workbook.Workbook()
ws = wb.active
ws.append(['标题', '链接', '媒体'])


def get_data(url, arguments):
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        response = requests.get(url, params=arguments, headers=header).json()
        return response
    except:
        sys.setrecursionlimit(10)
        get_data(url, arguments)


def parse_data(json_data):
    try:
        news_titles = jsonpath(json_data, '$..title')
        news_links = jsonpath(json_data, '$..url')
        news_names = jsonpath(json_data, '$..media_name')
        for news_title, news_link, news_name in zip(news_titles, news_links, news_names):
            save_data(news_title, news_link, news_name)
    except:
        sys.exit(1)


def save_data(news_title, news_link, news_name):
    my_list = [news_title, news_link, news_name]
    ws.append(my_list)
    wb.save('腾讯新闻.xlsx')


if __name__ == '__main__':
    url = "https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list"
    for i in range(0, 181, 20):
        arguments = {
            'sub_srv_id': '24hours',
            'srv_id': 'pc',
            'offset': f'{i}',
            'limit': '20',
            'strategy': '1',
            'ext': '{"pool": ["top", "hot"], "is_filter": 7, "check_type": true}'
        }
        data = get_data(url, arguments)
        parse_data(data)
