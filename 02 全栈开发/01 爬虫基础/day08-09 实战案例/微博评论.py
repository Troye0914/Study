import re
import csv
import sys
import time
import random
import requests
from jsonpath import jsonpath


class WeiBoSpider(object):
    tunnel = "a130.kdltps.com:15818"
    username = "t16908862605129"
    password = "zxcv6789"

    def __init__(self):
        # 一级评论url
        self.one_url = 'https://m.weibo.cn/comments/hotflow'
        self.one_data = {
            'id': '4813628149072458',
            'mid': '4813628149072458',
            'max_id': None,
            'max_id_type': '0'
        }
        self.headers = {
            'referer': 'https://m.weibo.cn/detail/4813628149072458?sudaref=login.sina.com.cn',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36',
            'cookie': '__bid_n=187ffb900226498b444207; SUB=_2A25JX1zaDeRhGeBO6FEQ8SrMyDuIHXVqoGSSrDV6PUJbkdANLWzFkW1NSgI3N31-5aa4uyY5pBBPOkBRebzIzS1g; _T_WM=73998776577; FPTOKEN=ueZtuEpAghJn25QBaL96Skacr48F4l23Sq7BL3V/F9B5pmFfNGf8MM3QPHhIKdjZ9h2qbh94+ztsKqYUsmb0g/HikUlk0YHz4lZkgCkkGJ1Y9RMewkX32njVFevRylmZduyhUzUWalJfIRYoufLi5NHWaZAgjedK3UwyW7AgvcoMCKvVcOY98bmd9Wv+reY7fFE55ToL2hBI+JendBEBM9SxBt8OLSb/uz8AGMPmwvaHgA06vWncD7fCjiCl7el17JMDi8g/fkqQJyF8dPQfZP1qxksPFXAb0rpD2hOlYsE58kH3hFI6RYL3KqSZJr01AoyeDsPXHh48syyiOhcK6De/NaVY+crabsgOJJLPHySD+6aeVzwUe6dyHjJX7/wdN+y+tHo23lUXkmGhN9E9aQ==|Iwdcsl+3Bx7s+nw+eh3eGsOzwcgIhSHVT6CG1nA2hBU=|10|e4fc630e68a611c5e6cde8d8f6071ae7; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4813628149072458%26luicode%3D20000061%26lfid%3D4813628149072458%26uicode%3D20000061%26fid%3D4813628149072458; XSRF-TOKEN=3c3414; WEIBOCN_FROM=1110006030; mweibo_short_token=c4c35a40da',
            'Accept-Encoding': 'gzip',
            'Connection': 'close'
        }
        self.proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": WeiBoSpider.username, "pwd": WeiBoSpider.password,
                                                            "proxy": WeiBoSpider.tunnel},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": WeiBoSpider.username, "pwd": WeiBoSpider.password,
                                                             "proxy": WeiBoSpider.tunnel}
        }

        # 二级评论url
        self.two_url = 'https://m.weibo.cn/comments/hotFlowChild'
        self.two_data = {
            'cid': '4813628329693567',
            'max_id': '0',
            'max_id_type': '0'
        }

        # 保存数据
        self.f = open('微博评论.csv', 'w', encoding='utf-8', newline='')
        self.csv_w = csv.writer(self.f)
        self.csv_w.writerow(['用户名', '一级评论', '二级评论'])
        # 存取二级评论
        self.two_text = ''

        # 评论条数
        self.one_count = 0
        self.two_count = 0

    def get_one_data(self):
        """获取一级评论并解析"""
        response = requests.get(self.one_url, headers=self.headers, params=self.one_data, proxies=self.proxies)
        json_data = response.json()
        one_comments = jsonpath(json_data, '$..data[0:19].text')
        one_authors = jsonpath(json_data, '$..data[0:19].user.screen_name')
        root_ids = jsonpath(json_data, '$..data[0:19].rootid')
        comment_tags = jsonpath(json_data, '$..data[0:19].comments')
        for one_author, one_comment, root_id, comment_tag in zip(one_authors, one_comments, root_ids, comment_tags):
            one_comment = re.sub('<.*?>', '', one_comment)
            self.one_count += 1
            print(f'正在爬取第{self.one_count}条一级评论 ==>')
            # 获取二级数据
            # 有一些一级评论下没有二级评论
            if not comment_tag:
                print('当前一级评论内不存在二级评论\n')
                # 将数据保存
                self.csv_w.writerow([one_author, one_comment, ''])
                self.two_text = ''
            else:
                # 更改二级评论的cid
                self.two_data['cid'] = root_id
                self.get_two_data()  # 二级爬取
                # 将数据保存
                self.csv_w.writerow([one_author, one_comment, self.two_text])
                self.two_text = ''

        # 一级评论翻页爬取
        # 获取响应报文中的max_id（用于下一页请求）
        max_id = jsonpath(json_data, '$..max_id')[0]
        try:
            # 更改请求参数
            self.one_data['max_id'] = max_id
            # 重新发起请求，同样的逻辑，直接递归调用
            time.sleep(random.randint(3, 6))  # 动态时间等待
            self.get_one_data()
        except:
            self.one_count = 0
            self.f.close()
            sys.exit('一级评论全部爬取完毕')

    def get_two_data(self):
        """获取二级评论并解析"""
        response = requests.get(self.two_url, headers=self.headers, params=self.two_data, proxies=self.proxies)
        json_data = response.json()
        two_comments = jsonpath(json_data, '$..data..text')
        two_authors = jsonpath(json_data, '$..data..screen_name')
        for two_author, two_comment in zip(two_authors, two_comments):
            two_comment = re.sub('<.*?>', '', two_comment)
            self.two_count += 1
            print(f'\t正在爬取第{self.two_count}条二级评论')
            # 添加所有二级数据
            self.two_text += two_comment + '\t'

        # 二级评论翻页爬取
        # 获取响应报文中的max_id（用于下一页请求）
        two_max_id = jsonpath(json_data, '$..max_id')[0]
        # 更改请求参数
        self.two_data['max_id'] = two_max_id
        # 重新发起请求，同样的逻辑，直接递归调用（二级翻页会结束，需要设置递归条件）
        if not two_max_id:
            print('二级评论全部爬取完毕\n')
            self.two_count = 0
        else:
            # 时间反爬
            time.sleep(random.randint(3, 6))  # 动态时间等待
            self.get_two_data()

    def run(self):
        self.get_one_data()


if __name__ == '__main__':
    wb = WeiBoSpider()
    wb.run()
